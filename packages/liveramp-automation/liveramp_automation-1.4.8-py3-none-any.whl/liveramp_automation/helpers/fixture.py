import os
import pytest
from selenium import webdriver
from liveramp_automation.helpers.file import FileHelper
from liveramp_automation.utils.allure import allure_page_screenshot, allure_drive_screenshot, allure_attach_video
from liveramp_automation.utils.log import Logger
from liveramp_automation.utils.time import fixed_wait
from typing import Generator
from dotenv import load_dotenv
from playwright.sync_api import Playwright, BrowserContext


##############################
# Resource Prefix Management #
#############################

@pytest.fixture(scope="session")
def res():
    """Get the configuration for the test environment.

    :return: Configuration dictionary for the test environment.
    """
    load_dotenv()
    Logger.debug("It is going to import the envChoice.")
    if not os.environ.get('ENVCHOICE'):
        os.environ['ENVCHOICE'] = "prod"
    run_on_env = os.environ['ENVCHOICE']
    Logger.debug("The testing environment is {} ".format(run_on_env))
    init_dict = FileHelper.read_init_file(os.getcwd(), 'pytest.ini')
    Logger.debug(init_dict)
    resource_path = None
    resource_prefix = None
    try:
        if init_dict and init_dict['data']:
            resource_data = init_dict['data']
            if resource_data['resource_path']:
                resource_path = resource_data['resource_path']
            else:
                resource_path = 'resources'
                Logger.warning("Use the resources as the default resource_path.")
            if resource_data['resource_prefix']:
                resource_prefix = resource_data['resource_prefix']
            else:
                resource_prefix = 'res'
                Logger.warning("Use the res as the default resource_prefix.")
    except TypeError:
        resource_path = 'resources'
        resource_prefix = 'res'
        Logger.warning("Use the resource and res as the default resource_path and resource_prefix.")
    return FileHelper.load_env_yaml(resource_path, resource_prefix, run_on_env)


###############################################################################################################
# API Prefix Management # We consider it's better to add the fixture methods to your own conftest.py
##############################################################################################################


################################################
# UI Automation Testing Prefix Management #
###############################################
@pytest.fixture(scope="session")
def driver():
    """Pytest fixture that provides a Selenium WebDriver instance for testing.
        Yields:
            WebDriver: A Selenium WebDriver instance for testing purposes.
    """
    load_dotenv()
    if not os.environ.get('runEnv'):
        os.environ['runEnv'] = "remote"
    run_on_env = os.environ['runEnv']
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    config_data = FileHelper.read_init_file(os.getcwd(), "pytest.ini", "r")
    Logger.debug(config_data)
    download_dir = config_data.get('download', 'reports/download')
    default_directory = os.path.join(os.getcwd(), download_dir)
    prefs = {"download.default_directory": default_directory}
    chrome_options.add_experimental_option("prefs", prefs)
    Logger.debug("The run Env is {}".format(run_on_env))
    Logger.debug("Run WEBDriver on lang=en ")
    chrome_options.add_argument('--lang=en')

    if run_on_env == "remote":
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('window-size=1920x1480')
    else:
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('window-size=1920x1480')

    driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    Logger.debug("We are going to open a blank page.")
    driver.get("about:blank")
    driver.implicitly_wait(30)
    Logger.debug("Started a ChromeDriver.")
    yield driver
    driver.close()
    Logger.debug("Closed the ChromeDriver.Goodbye!")


@pytest.fixture(scope="session")
def page(playwright: Playwright) -> Generator[BrowserContext, None, None]:
    """ Pytest fixture that provides a Playwright BrowserContext for testing.
       Args:
           playwright (Playwright): Playwright instance.
       Yields:
           BrowserContext: A Playwright BrowserContext for testing purposes.
    """
    load_dotenv()
    if not os.environ.get('runEnv'):
        os.environ['runEnv'] = "remote"
    config_data = FileHelper.read_init_file(os.getcwd(), "pytest.ini", "r")
    Logger.debug(config_data)
    download_dir = config_data.get('download', 'reports/download')
    default_directory = os.path.join(os.getcwd(), download_dir)
    recording_dir = config_data.get('download', 'reports')
    recording_directory = os.path.join(os.getcwd(), recording_dir)
    if os.environ['runEnv'] == "remote":
        browser_context = playwright.chromium.launch_persistent_context("", headless=True,
                                                                        downloads_path=default_directory,
                                                                        record_video_dir=recording_directory,
                                                                        viewport={"width": 1920, "height": 1080},
                                                                        args=['--lang=en'])
    else:
        browser_context = playwright.chromium.launch_persistent_context("", headless=False,
                                                                        downloads_path=default_directory,
                                                                        record_video_dir=recording_directory,
                                                                        viewport={"width": 1920, "height": 1080},
                                                                        args=['--lang=en'])
    # Start tracing before creating / navigating a page.
    browser_context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = browser_context.pages[0]
    page.set_default_timeout(60000)
    yield page
    page.close()
    browser_context.tracing.stop(path=os.path.join(os.getcwd(), recording_dir, "trace.zip"))
    browser_context.close()
    fixed_wait()
    files = os.listdir(recording_directory)
    webm_files = [file for file in files if file.endswith(".webm")]
    recording_path = os.path.join(os.getcwd(), "reports", webm_files[0])
    allure_attach_video("Recording_video", recording_path)


@pytest.hookimpl(hookwrapper=True)
def pytest_bdd_step_error(feature, scenario, step, step_func_args, exception):
    """
    This hook is called when there is an error during the execution of a step.
    It takes a screenshot of the current page if the step fails.
    """
    try:
        outcome = yield
        Logger.debug(f"Step error in scenario '{outcome.excinfo}'.")
        Logger.error(f"Step error in scenario '{scenario.name}' at step '{step.keyword} {step.name}': {exception}")
        screenshot_name = f"screenshot_{feature.name}_{scenario.name}_{step.keyword}_{step.name}"
        if 'page' in step_func_args.keys():
            allure_page_screenshot(step_func_args['page'], screenshot_name)
        elif 'driver' in step_func_args.keys():
            allure_drive_screenshot(step_func_args['driver'], screenshot_name)
        else:
            Logger.debug("No need to take screenshot")
    except exception:
        pass


@pytest.hookimpl(hookwrapper=True)
def pytest_bdd_before_scenario(request, feature, scenario):
    outcome = yield
    os.environ["SCENARIO_NAME"] = scenario.name


@pytest.fixture(scope="session")
def request_config():
    return {
        "request_url": None,
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "Method": "Get",
        "request_body": None,
        "response_body": None
    }
