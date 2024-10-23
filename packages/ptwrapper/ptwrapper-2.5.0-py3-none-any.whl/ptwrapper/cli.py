import os
import json
import sys
import glob
import shutil as sh
from argparse import ArgumentParser

from .utils import remove_directory_if_empty
from .utils import dict_to_html_table

from osve import osve

from .main import simulation

def cli(test=False):
    """
    CLI to resolve a PTR file and generate a SPICE CK kernel.

    Parameters
    ----------
    test : bool, optional
        If True, return the argument parser for testing (default is False).
    """
    parser = ArgumentParser(description='Pointing Tool Wrapper (PTWrapper) simulates a PTR and generates the '
                                        'corresponding resolved PTR, SPICE CK kernels, '
                                        'and other attitude related files. PTWrapper uses OSVE to simulate the PTR.')

    parser.add_argument("-m", "--meta-kernel", help="[MANDATORY] Path to the SPICE Meta-kernel (MK) file")
    parser.add_argument("-p", "--ptr", help="[MANDATORY] Path to the Pointing Timeline Request (PTR) file.")
    parser.add_argument("-w", "--working-dir", default=os.getcwd(),
                        help="Path to the working directory. Default is the current directory.")
    parser.add_argument("-o", "--output-dir", help="Path to the output directory. Overwrites "
                        "default output file names. Default is the current directory. Directory names: input, "
                        "output, and config are reserved; they can be used at your own risk.")
    parser.add_argument("-t", "--time-step", default=5,
                        help="Output CK file time step in seconds. Default is 5s.")
    parser.add_argument("-np", "--no-power", action="store_true", help="Indicates not to calculate available power. "
                        "Default is that the Available Power will be computed.")
    parser.add_argument("-sa", "--sa-ck", action="store_true", help="Generate the Solar Arrays SPICE CK. "
                        "Default is that the SA CK is not generated.")
    parser.add_argument("-mga", "--mga-ck", action="store_true", help="Generate the Medium Gain Antenna SPICE CK. "
                        "Default is that the MGA CK is not generated.")
    parser.add_argument("-q", "--quaternions", action="store_true", help="Calculate the quaternions. "
                        "Default is that the quaternions will not be computed.")
    parser.add_argument("-f", "--fixed-definitions",
                        help="Print the AGM Fixed Definitions in use for PTR design.",
                        action="store_true")
    parser.add_argument("-nc", "--no-cleanup",
                        help="Indicates not to cleanup the output directory and keep the OSVE output structure.",
                        action="store_true")
    parser.add_argument("-v", "--version",
                        help="OSVE, AGM, and EPS libraries version.",
                        action="store_true")

    args = parser.parse_args()

    # Process the arguments and perform further actions
    if args.version:
        the_osve = osve.osve()
        print("")
        print("OSVE LIB VERSION:       ", the_osve.get_app_version())
        print("OSVE AGM VERSION:       ", the_osve.get_agm_version())
        print("OSVE EPS VERSION:       ", the_osve.get_eps_version())
        print("")
        sys.exit(1)

    if args.fixed_definitions:
        fixed_definitions_filepath = os.path.join(
            os.path.dirname(__file__), "config/age", "cfg_agm_jui_fixed_definitions.xml"
        )
        try:
            with open(fixed_definitions_filepath, 'r') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print(f'[ERROR]    {"<PTWR>":<27} The file could not be found.')
        except Exception as e:
            print(f'[ERROR]    {"<PTWR>":<27} An error occurred:', e)
        sys.exit(1)

    if args.meta_kernel:
        if not os.path.exists(args.meta_kernel):
            raise ValueError(f'[ERROR]    {"<PTWR>":<27} Meta-kernel does not exist')
    else:
        raise ValueError(f'[ERROR]    {"<PTWR>":<27} Meta-kernel not provided')

    if args.ptr:
        ptr_file = os.path.split(args.ptr)[-1]
        fname, ext = os.path.splitext(ptr_file)
        ext = ext.lower()
        if ext not in ['.xml', '.ptx', '.ptr']:
            raise ValueError(f'[ERROR]    {"<PTWR>":<27} Input PTR extension incorrect (not .xml, .XML ,.ptr, .PTR, .ptx or .PTX)')
        with open(args.ptr, 'r') as p:
            ptr_content = p.read()
    else:
        raise ValueError(f'[ERROR]    {"<PTWR>":<27} PTR/PTX file not provided')

    print(f'[INFO]    {"<PTWR>":<27} PTWrapper session execution')

    session_file_path, root_scenario_path, ptr_log = simulation(args.meta_kernel, ptr_content, working_dir=args.working_dir,
                                                                time_step=int(args.time_step),
                                                                no_power=args.no_power,
                                                                sa_ck=args.sa_ck,
                                                                mga_ck=args.mga_ck,
                                                                quaternions=args.quaternions)

    if ptr_log == -1:
        print(f'[ERROR]   {"<PTWR>":<27} PTWrapper session ended with ERRORS check your input files')
        if test:
            return parser
        return sys.exit(-1)

    if args.output_dir:
        # Post-process the result
        output_dir = os.path.abspath(args.output_dir)
    else:
        output_dir = os.getcwd()

    # Create the PTR JSON/HTML log
    if ptr_log:
        print(f'[INFO]    {"<PTWR>":<27} Creating the HTML PTR log {fname}_ptr_log.html')
        html_content = dict_to_html_table(ptr_log)
        file_name = os.path.join(output_dir, f'{fname}_ptr_log.html')

        with open(file_name, 'w') as file:
            file.write(html_content)

        # Write the JSON content to a file
        print(f'[INFO]    {"<PTWR>":<27} Creating the JSON PTR log {fname}_ptr_log.json')
        file_name = os.path.join(output_dir, f'{fname}_ptr_log.json')

        with open(file_name, "w") as file:
            json.dump(ptr_log, file)
    else:
        print(f'[INFO]    {"<PTWR>":<27} The PTR has no errors, no PTR log is created')

    if args.quaternions:
        print(f'[INFO]    {"<PTWR>":<27} Renaming quaternions.csv to {fname}_quaternions.csv')
        sh.move(os.path.join(root_scenario_path, 'output', 'quaternions.csv'),
                os.path.join(output_dir, f'{fname}_quaternions.csv'))

    if args.sa_ck:
        sa_bc_path = os.path.join(root_scenario_path, 'output', 'juice_sa_ptr.bc')
        if os.path.exists(sa_bc_path):
            print(f'[INFO]    {"<PTWR>":<27} Renaming juice_sa_ptr.bc/csv to juice_sa_{fname}.bc/csv')
            sh.move(sa_bc_path, os.path.join(output_dir, f'juice_sa_{fname}.bc'))
            sh.move(os.path.join(root_scenario_path, 'output', 'juice_sa_ptr.csv'),
                    os.path.join(output_dir, f'juice_sa_{fname}.csv'))
        else:
            print(f'[INFO]    {"<PTWR>":<27} SA CSV and CK files not generated.')

    if args.mga_ck:
        mga_bc_path = os.path.join(root_scenario_path, 'output', 'juice_mga_ptr.bc')
        if os.path.exists(mga_bc_path):
            print(f'[INFO]    {"<PTWR>":<27} Renaming juice_mga_ptr.bc/csv to juice_mga_{fname}.bc/csv')
            sh.move(mga_bc_path, os.path.join(output_dir, f'juice_mga_{fname}.bc'))
            sh.move(os.path.join(root_scenario_path, 'output', 'juice_mga_ptr.csv'),
                    os.path.join(output_dir, f'juice_mga_{fname}.csv'))
        else:
            print(f'[INFO]    {"<PTWR>":<27} MGA CSV and CK files not generated.')

    if not args.no_power:
        print(f'[INFO]    {"<PTWR>":<27} Renaming power.csv to {fname}_power.csv')
        sh.move(os.path.join(root_scenario_path, 'output', 'power.csv'),
                os.path.join(output_dir, f'{fname}_power.csv'))

    print(f'[INFO]    {"<PTWR>":<27} Renaming ptr_resolved.ptx to {fname}_resolved.ptx')
    sh.move(os.path.join(root_scenario_path, 'output', 'ptr_resolved.ptx'),
            os.path.join(output_dir, f'{fname}_resolved.ptx'))

    print(f'[INFO]    {"<PTWR>":<27} Renaming juice_sc_ptr.bc to juice_sc_{fname.lower()}_v01.bc')
    sh.move(os.path.join(root_scenario_path, 'output', 'juice_sc_ptr.bc'),
            os.path.join(output_dir, f'juice_sc_{fname.lower()}_v01.bc'))

    print(f'[INFO]    {"<PTWR>":<27} Renaming log.json to {fname}_osve_log.json')
    sh.move(os.path.join(root_scenario_path, 'output', 'log.json'),
            os.path.join(output_dir, f'{fname}_osve_log.json'))


    if not args.no_cleanup:
        print(f'[INFO]    {"<PTWR>":<27} Cleaning up OSVE execution files and directories')
        os.remove(os.path.join(root_scenario_path, 'input', 'PTR_PT_V1.ptx'))
        os.remove(os.path.join(root_scenario_path, 'input', 'downlink.evf'))
        for f in glob.glob(os.path.join(root_scenario_path, 'input', f'TOP_*_events.evf')):
            os.remove(f)
        for f in glob.glob(os.path.join(root_scenario_path, 'input', f'EVT_*_GEOPIPELINE.EVF')):
            os.remove(f)
        sh.rmtree(os.path.join(root_scenario_path, 'input', 'edf'))
        sh.rmtree(os.path.join(root_scenario_path, 'input', 'evf'))
        sh.rmtree(os.path.join(root_scenario_path, 'input', 'itl'))
        os.remove(os.path.join(root_scenario_path, 'session_file.json'))
        sh.rmtree(os.path.join(root_scenario_path, 'config', 'age'))
        sh.rmtree(os.path.join(root_scenario_path, 'config', 'ise'))

        mkname = os.path.split(args.meta_kernel)[-1]

        if args.meta_kernel != os.path.join(root_scenario_path, 'kernel', mkname):
            os.remove(os.path.join(root_scenario_path, 'kernel', mkname))

        for directory in ['kernel', 'output', 'input', 'config']:
            remove_directory_if_empty(os.path.join(root_scenario_path, directory))

    print(f'[INFO]    {"<PTWR>":<27} PTWrapper session ended successfully')

    if test:
        return parser
