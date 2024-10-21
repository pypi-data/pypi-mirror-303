from ..abstract_webtools import *
from .urlManager import *
from .requestManager import *
class soupManager:
    """
    SoupManager is a class for managing and parsing HTML source code using BeautifulSoup.

    Args:
        url (str or None): The URL to be parsed (default is None).
        source_code (str or None): The HTML source code (default is None).
        url_mgr (UrlManager or None): An instance of UrlManager (default is None).
        requestManager (SafeRequest or None): An instance of SafeRequest (default is None).
        parse_type (str): The type of parser to be used by BeautifulSoup (default is "html.parser").

    Methods:
        re_initialize(): Reinitialize the SoupManager with the current settings.
        update_url(url): Update the URL and reinitialize the SoupManager.
        update_source_code(source_code): Update the source code and reinitialize the SoupManager.
        update_requestManager(requestManager): Update the request manager and reinitialize the SoupManager.
        update_url_mgr(url_mgr): Update the URL manager and reinitialize the SoupManager.
        update_parse_type(parse_type): Update the parsing type and reinitialize the SoupManager.
        all_links: A property that provides access to all discovered links.
        _all_links_get(): A method to load all discovered links.
        get_all_website_links(tag="a", attr="href"): Get all URLs belonging to the same website.
        meta_tags: A property that provides access to all discovered meta tags.
        _meta_tags_get(): A method to load all discovered meta tags.
        get_meta_tags(): Get all meta tags in the source code.
        find_all(element, soup=None): Find all instances of an HTML element in the source code.
        get_class(class_name, soup=None): Get the specified class from the HTML source code.
        has_attributes(tag, *attrs): Check if an HTML tag has the specified attributes.
        get_find_all_with_attributes(*attrs): Find all HTML tags with specified attributes.
        get_all_desired_soup(tag=None, attr=None, attr_value=None): Get HTML tags based on specified criteria.
        extract_elements(url, tag=None, class_name=None, class_value=None): Extract portions of source code based on filters.
        find_all_with_attributes(class_name=None, *attrs): Find classes with associated href or src attributes.
        get_images(tag_name, class_name, class_value): Get images with specific class and attribute values.
        discover_classes_and_meta_images(tag_name, class_name_1, class_name_2, class_value, attrs): Discover classes and meta images.

    Note:
        - The SoupManager class is designed for parsing HTML source code using BeautifulSoup.
        - It provides various methods to extract data and discover elements within the source code.
    """
    def __init__(self,url=None,source_code=None,url_mgr=None,req_mgr=None, parse_type="html.parser"):
        self.soup=[]
        self.url_mgr = get_url_mgr(url=url,url_mgr=url_mgr)
        self.url=self.url_mgr.url
        self.req_mgr = get_req_mgr(req_mgr=req_mgr,url=self.url,url_mgr=self.url_mgr,source_code=source_code)
        self.parse_type = parse_type
        source_code = source_code or self.req_mgr.source_code or self.req_mgr.source_code_bytes
        if source_code:
            source_code = str(source_code)
        self.source_code = source_code
        self.soup= BeautifulSoup(self.source_code, self.parse_type)
        self._all_links_data = None
        self._meta_tags_data = None
    def re_initialize(self):
        self.soup= BeautifulSoup(self.source_code, self.parse_type)
        self._all_links_data = None
        self._meta_tags_data = None
    def update_url(self,url):
        self.url_mgr.update_url(url=url)
        self.url=self.url_mgr.url
        self.req_mgr.update_url(url=url)
        self.source_code = self.req_mgr.source_code_bytes
        self.re_initialize()
    def update_source_code(self,source_code):
        if source_code:
            source_code = str(source_code)
        self.source_code = source_code
        self.re_initialize()
    def update_requestManager(self,requestManager):
        self.req_mgr = requestManager
        self.url_mgr=self.req_mgr.url_mgr
        self.url=self.url_mgr.url
        self.source_code = self.req_mgr.source_code_bytes
        self.re_initialize()
    def update_url_mgr(self,url_mgr):
        self.url_mgr=url_mgr
        self.url=self.url_mgr.url
        self.req_mgr.update_url_mgr(url_mgr=self.url_mgr)
        self.source_code = self.req_mgr.source_code_bytes
        self.re_initialize()
    def update_parse_type(self,parse_type):
        self.parse_type=parse_type
        self.re_initialize()
    @property
    def all_links(self):
        """This is a property that provides access to the _all_links_data attribute.
        The first time it's accessed, it will load the data."""
        if self._all_links_data is None:
            print("Loading all links for the first time...")
            self._all_links_data = self._all_links_get()
        return self._all_links_data
    def _all_links_get(self):
        """A method that loads the data (can be replaced with whatever data loading logic you have)."""
        return self.get_all_website_links()
    def get_all_website_links(self,tag="a",attr="href") -> list:
        """
        Returns all URLs that are found on the specified URL and belong to the same website.

        Args:
            url (str): The URL to search for links.

        Returns:
            list: A list of URLs that belong to the same website as the specified URL.
        """
        all_urls=[self.url_mgr.url]
        domain = self.url_mgr.domain
        all_desired=self.get_all_desired_soup(tag=tag,attr=attr)
        for tag in all_desired:
            href = tag.attrs.get(attr)
            if href == "" or href is None:
                # href empty tag
                continue
            href=self.url_mgr.get_relative_href(self.url_mgr.url,href)
            if not self.url_mgr.is_valid_url(href):
                # not a valid URL
                continue
            if href in all_urls:
                # already in the set
                continue
            if domain not in href:
                # external link
                continue
            all_urls.append(href)
                
        return all_urls


    @property
    def meta_tags(self):
        """This is a property that provides access to the _all_links_data attribute.
        The first time it's accessed, it will load the data."""
        if self._meta_tags_data is None:
            print("Loading all links for the first time...")
            self._meta_tags_data = self._all_links_get()
        return self._meta_tags_data
    def _meta_tags_get(self):
        """A method that loads the data (can be replaced with whatever data loading logic you have)."""
        return self.get_meta_tags()
    def get_meta_tags(self):
        tags = self.find_all("meta")
        for meta_tag in tags:
            for attr, values in meta_tag.attrs.items():
                if attr not in self.meta_tags:
                    self.meta_tags[attr] = []
                if values not in self.meta_tags[attr]:
                    self.meta_tags[attr].append(values)

                    
    def find_all(self,element,soup=None):
        soup = self.soup if soup == None else soup
        return soup.find_all(element)
    def get_class(self,class_name,soup=None):
        soup = self.soup if soup == None else soup
        return soup.get(class_name)
    @staticmethod
    def has_attributes(tag, *attrs):
        return any(tag.has_attr(attr) for attr in attrs)
    def get_find_all_with_attributes(self, *attrs):
        return self.soup.find_all(lambda t: self.has_attributes(t, *attrs))
    def find_tags_by_attributes(self, tag: str = None, attr: str = None, attr_values: List[str] = None) ->List:
        if not tag:
            tags = self.soup.find_all(True)  # get all tags
        else:
            tags = self.soup.find_all(tag)  # get specific tags
            
        extracted_tags = []
        for t in tags:
            if attr:
                attribute_value = t.get(attr)
                if not attribute_value:  # skip tags without the desired attribute
                    continue
                if attr_values and not any(value in attribute_value for value in attr_values):  # skip tags without any of the desired attribute values
                    continue
            extracted_tags.append(t)
        return extracted_tags


    def extract_elements(self,url:str=None, tag:str=None, class_name:str=None, class_value:str=None) -> list:
        """
        Extracts portions of the source code from the specified URL based on provided filters.

        Args:
            url (str): The URL to fetch the source code from.
            element_type (str, optional): The HTML element type to filter by. Defaults to None.
            attribute_name (str, optional): The attribute name to filter by. Defaults to None.
            class_name (str, optional): The class name to filter by. Defaults to None.

        Returns:
            list: A list of strings containing portions of the source code that match the provided filters.
        """
        elements = []
        # If no filters are provided, return the entire source code
        if not tag and not class_name and not class_value:
            elements.append(str(self.soup))
            return elements
        # Find elements based on the filters provided
        if tag:
            elements.extend([str(tags) for tags in self.get_all_desired(tag)])
        if class_name:
            elements.extend([str(tags) for tags in self.get_all_desired(tag={class_name: True})])
        if class_value:
            elements.extend([str(tags) for tags in self.get_all_desired(class_name=class_name)])
        return elements
    def find_all_with_attributes(self, class_name=None, *attrs):
        """
        Discovers classes in the HTML content of the provided URL 
        that have associated href or src attributes.

        Args:
            base_url (str): The URL from which to discover classes.

        Returns:
            set: A set of unique class names.
        """

    
        unique_classes = set()
        for tag in self.get_find_all_with_attributes(*attrs):
            class_list = self.get_class(class_name=class_name, soup=tag)
            unique_classes.update(class_list)
        return unique_classes
    def get_images(self, tag_name, class_name, class_value):
        images = []
        for tag in self.soup.find_all(tag_name):
            if class_name in tag.attrs and tag.attrs[class_name] == class_value:
                content = tag.attrs.get('content', '')
                if content:
                    images.append(content)
        return images
    def extract_text_sections(self) -> list:
        """
        Extract all sections of text from an HTML content using BeautifulSoup.

        Args:
            html_content (str): The HTML content to be parsed.

        Returns:
            list: A list containing all sections of text.
        """
        # Remove any script or style elements to avoid extracting JavaScript or CSS code
        for script in self.soup(['script', 'style']):
            script.decompose()

        # Extract text from the remaining elements
        text_sections = self.soup.stripped_strings
        return [text for text in text_sections if text]
    def discover_classes_and_meta_images(self, tag_name, class_name_1, class_name_2, class_value, attrs):
        """
        Discovers classes in the HTML content of the provided URL 
        that have associated href or src attributes. Also, fetches 
        image references from meta tags.

        Args:
            base_url (str): The URL from which to discover classes and meta images.

        Returns:
            tuple: A set of unique class names and a list of meta images.
        """
    
        unique_classes = self.find_all_with_attributes(class_name=class_name_1, *attrs)
        images = self.get_images(tag_name=tag_name, class_name=class_name_2, class_value=class_value)
        return unique_classes, images
    def get_all_tags_and_attribute_names(self):
        tag_names = set()  # Using a set to ensure uniqueness
        attribute_names = set()
        get_all = self.find_tags_by_attributes()
        for tag in get_all:  # True matches all tags
            tag_names.add(tag.name)
            for attr in tag.attrs:
                attribute_names.add(attr)
        tag_names_list = list(tag_names)
        attribute_names_list = list(attribute_names)
        return {"tags":tag_names_list,"attributes":attribute_names_list}

    def get_all_attribute_values(self):
        attribute_values={}
        get_all = self.find_tags_by_attributes()
        for tag in get_all:  # True matches all tags
            for attr, value in tag.attrs.items():
                # If attribute is not yet in the dictionary, add it with an empty set
                if attr not in attribute_values:
                    attribute_values[attr] = set()
                # If the attribute value is a list (e.g., class), extend the set with the list
                if isinstance(value, list):
                    attribute_values[attr].update(value)
                else:
                    attribute_values[attr].add(value)
        for attr, values in attribute_values.items():
            attribute_values[attr] = list(values)
        return attribute_values
    
    @property
    def url(self):
        return self._url
    @url.setter
    def url(self, new_url):
        self._url = new_url

class SoupManagerSingleton():
    _instance = None
    @staticmethod
    def get_instance(url_mgr,requestManager,parse_type="html.parser",source_code=None):
        if SoupManagerSingleton._instance is None:
            SoupManagerSingleton._instance = SoupManager(url_mgr,requestManager,parse_type=parse_type,source_code=source_code)
        elif parse_type != SoupManagerSingleton._instance.parse_type  or source_code != SoupManagerSingleton._instance.source_code:
            SoupManagerSingleton._instance = SoupManager(url_mgr,requestManager,parse_type=parse_type,source_code=source_code)
        return SoupManagerSingleton._instance
def get_soup_mgr(url=None,url_mgr=None,source_code=None,req_mgr=None,soup_mgr=None):
    url_mgr = get_url_mgr(url=url,url_mgr=url_mgr)
    req_mgr = get_req_mgr(url_mgr=url_mgr,source_code=source_code)
    soup_mgr = soup_mgr or soupManager(url_mgr=url_mgr,req_mgr=req_mgr)
    return soup_mgr
