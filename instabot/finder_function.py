from web_elements import xpath
from web_elements import selector 

def read_xpath(function_name, xpath_name):
    return xpath[function_name][xpath_name]
    
def read_selector(function_name,selector_name):
    return selector[function_name][selector_name]