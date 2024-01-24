class IOSCapabilities:
    DESIRED_CAP_IPA = {
        'deviceName': 'iPhone 15',
        'platformName': 'iOS',
        'version': '17.2',
        'app': '/Users/aslan/PetProjects/appiumProject/testAppFromLambdaSimulator/Payload/LambdaUiKitIOS.app',
        'automationName': 'XCUITest',
    }

    DEBUG_CAPABILITIES = {
        'platformName': 'Ios',
        'udid': 'D95B11D3-6825-40F2-BBBE-8222B08D0B89',  # Here you should add id of simulator
        'automationName': 'XCUITest',
    }

    DESIRED_CAPABILITIES_TESTING_BOT = {
        "build": "REAL DEVICE",
        "name": "helloWorldTest",
        'deviceName': 'iPhone XR',
        'platformName': 'iOS',
        'version': '16.3',
        'realDevice': True,
        'app': 'tb://954fcb23b52a1be4e20e0ec5',
        'automationName': 'XCUITest'
    }

    DESIRED_CAPABILITIES_EMULATOR_HELLO_WORLD = {
        "build": "Simulator IOS",
        "name": "helloWorldTest",
        "deviceName": "iPhone 15",
        "platformName": "iOS",
        'realDevice': False,
        "version": "17.2",
        "app": "tb://0a594428d1ea43611a9eaed9",
        "automationName": "XCUITest"
    }

    DESIRED_CAPABILITIES_REAL_LAMBDA = {
        "build": "REAL DEVICE",
        "name": "helloWorldTest",
        "deviceName": "iPhone 12",
        "platformName": "iOS",
        "platformVersion": "14",
        'isRealMobile': True,
        'app': 'tb://cd3ea71e39ab49e500857598',
        'automationName': 'XCUITest',
        'browserName': 'safari',
        "network": False,
        "visual": True,
        "video": True

    }

    DESIRED_CAPABILITIES_SIMULATOR_HELLO_WORLD_LAMBDA = {
        "deviceName": "iPhone 12",
        "platformName": "ios",
        "platformVersion": "14",
        "isRealMobile": False,
        "app": "lt://proverbial-ios",  # Enter app_url here
        "build": "Python Vanilla iOS",
        "name": "Sample Test - Python",
        "network": False,
        "visual": True,
        "video": True
        # "w3c": True,
        # 'app': 'tb://cd3ea71e39ab49e500857598',
        # "platformName": "ios",
        # "isRealMobile": False,
        # "deviceName": "iPhone 12",
        # "platformVersion": "14",
        # "deviceOrientation": "PORTRAIT",
    }


class AndroidCapabilities:
    pass
