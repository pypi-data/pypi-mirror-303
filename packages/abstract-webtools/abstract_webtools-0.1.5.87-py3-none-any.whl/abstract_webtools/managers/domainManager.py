from ..abstract_webtools import *
class domainManager(metaclass=SingletonMeta):
    def __init__(self, url):
        if not hasattr(self, 'initialized'):  # Prevent reinitialization
            self.initialized = True
            parsed_url = urlparse(url)
            self.domain = parsed_url.netloc
            self.scheme = parsed_url.scheme
    def get_url_to_path(self, url):
        url = eatAll(str(url),['',' ','\n','\t','\\','/'])
        parsed_url = urlparse(url)
        if 'data:image' in url:
            input(url)
        if parsed_url.netloc == self.domain:
            paths = parsed_url.path.split('/')
            dir_path =self.site_dir
            for path in paths[:-1]:
                dir_path = os.path.join(dir_path, path)
                os.makedirs(dir_path, exist_ok=True)
        #if 'svg' in url:
        #$    input(url)
         #   dir_path = get_image_name('contents',directory=dir_path,ext='png',url=item_url)


            self.page_type.append(os.path.splitext(paths[-1])[-1] or 'html' if len(self.page_type) == 0 else self.page_type[-1])
            
            dir_path = os.path.join(dir_path, paths[-1])
            return dir_path

    def saved_url_check(self, url):
  
        path = self.get_url_to_path(url)
        return path

    def get_with_netloc(self, url):
        parsed_url = urlparse(url)
        if parsed_url.netloc == '':
            url = f"{self.scheme}://{self.domain}/{url.strip()}"
        return url

    def get_driver(self, url):
        if url and url not in self.drivers:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(options=chrome_options)
            self.drivers[url] = driver
            driver.get(url)
        return self.drivers[url]
