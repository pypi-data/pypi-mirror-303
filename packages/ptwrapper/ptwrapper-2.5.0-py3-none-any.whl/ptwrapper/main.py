import os

from .utils import create_structure
from .utils import OsvePtrLogger

from osve import osve


def execute(root_scenario_path, session_file_path):
    """
    Executes the OSVE simulation for the given scenario and session file.

    This function initializes the OSVE simulator, registers the logger
    as both a subscriber and a logger, and then executes the simulation
    using the specified scenario and session file.

    Parameters:
    -----------
    root_scenario_path : str
        The file path to the root scenario directory.
    session_file_path : str
        The file path to the session configuration file.

    Returns:
    --------
    execution : object
        The result of the OSVE simulation execution.
    """
    sim = osve.osve()

    theOsvePtrLogger = OsvePtrLogger()
    sim.register_subscriber(theOsvePtrLogger)
    sim.register_logger(theOsvePtrLogger)

    execution = sim.execute(root_scenario_path, session_file_path)

    ptr_log = theOsvePtrLogger.log(verbose=False)

    return execution, ptr_log


def simulation(mk, ptr_content, working_dir='.', time_step=30, no_power=False, sa_ck=False, mga_ck=False,
            quaternions=False):
    """
    Calls the OSVE simulation for the given metakernel, PTR content, and options.

    Parameters
    ----------
    mk : str
        Path to the metakernel file required by the simulation.
    ptr_content : str
        PTR content to be executed in the simulation.
    working_dir : str, optional
        The directory in which to create the simulation structure (default is current directory).
    time_step : int, optional
        Time step interval for the simulation (default is 30 seconds).
    no_power : bool, optional
        Disable power calculations during the simulation (default is False).
    sa_ck : bool, optional
        Use solar array CK file during the simulation (default is False).
    mga_ck : bool, optional
        Use MGA CK file during the simulation (default is False).
    quaternions : bool, optional
        Include quaternions in the simulation output (default is False).

    Returns
    -------
    tuple
        session_file_path : str
            Path to the created session file.
        root_scenario_path : str
            Path to the root scenario directory.
        ptr_log : dict or int
            The log generated from PTR execution, or -1 if execution failed.
    """

    # Step 1: Create the necessary simulation structure
    session_file_path = create_structure(working_dir, mk, ptr_content,
                                         step=time_step,
                                         no_power=no_power,
                                         sa_ck=sa_ck,
                                         mga_ck=mga_ck,
                                         quaternions=quaternions)

    # Get the root directory of the scenario based on the session file path
    root_scenario_path = os.path.dirname(session_file_path)

    # Step 2: Execute OSVE
    execution, ptr_log = execute(root_scenario_path, session_file_path)

    # Step 3: Check if the execution was successful, return early if it failed
    if execution != 0:
        return session_file_path, root_scenario_path, -1

    return session_file_path, root_scenario_path, ptr_log



