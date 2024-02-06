import xml.etree.ElementTree as ET

def load_network_configuration():
    config_path = '../data/myNetworkConfig.xml'
    tree = ET.parse(config_path)
    root = tree.getroot()
    # Process your XML data as needed

# Remember to call your function appropriately