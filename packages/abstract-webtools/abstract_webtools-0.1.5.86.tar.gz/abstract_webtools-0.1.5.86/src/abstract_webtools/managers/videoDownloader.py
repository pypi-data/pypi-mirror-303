import os
class VideoDownloader:
    """
    VideoDownloader is a class for downloading videos from URLs using YouTube-DL.

    Args:
        link (str or list): The URL(s) of the video(s) to be downloaded.
        temp_directory (str or None): The directory to store temporary video files (default is None, uses video_directory/temp_files).
        video_directory (str or None): The directory to store downloaded videos (default is None, uses 'videos' in the current working directory).
        remove_existing (bool): Whether to remove existing video files with the same name (default is True).

    Methods:
        count_outliers(speed, threshold): Count speed outliers below the threshold.
        filter_outliers(speeds): Filter out speed outliers in the list of speeds.
        remove_temps(file_name): Remove temporary video files based on the file name.
        move_video(): Move the downloaded video to the final directory.
        yt_dlp_downloader(url, ydl_opts={}, download=True): Download video information using YouTube-DL.
        progress_callback(d): Callback function to monitor download progress.
        download(): Download video(s) based on the provided URL(s).
        monitor(): Monitor the download progress.
        start(): Start the download and monitoring threads.

    Note:
        - The VideoDownloader class uses YouTube-DL to download videos.
        - It allows downloading from multiple URLs.
        - You need to have YouTube-DL installed to use this class.
    """
    def __init__(self, link,temp_directory=None,video_directory=None,remove_existing=True):
        if video_directory==None:
            video_directory=os.path.join(os.getcwd(),'videos')
        if temp_directory == None:
            temp_directory=os.path.join(video_directory,'temp_files')
        self.thread_manager = ThreadManager()
        self.pause_event = self.thread_manager.add_thread('pause_event')
        self.link = link
        self.temp_directory = temp_directory
        self.video_directory = video_directory
        self.remove_existing=remove_existing
        self.video_urls=self.link if isinstance(self.link,list) else [self.link]
        self.starttime = None
        self.downloaded = 0
        self.time_interval=60
        self.monitoring=True
        self.temp_file_name = None
        self.file_name = None
        self.dl_speed = None
        self.dl_eta=None
        self.total_bytes_est=None
        self.percent_speed=None
        self.percent=None
        self.speed_track = []
        self.video_url=None
        self.last_checked = get_time_stamp()
        self.num=0
        self.start()
    def count_outliers(self,speed,threshold):
        if speed < threshold:
            self.outlier_count+=1
        else:
            self.outlier_count=0
    def filter_outliers(self,speeds):
        # Step 1: Compute initial average
        initial_avg = sum(speeds) / len(speeds)
        
        # Step 2: Remove speeds 25% under the average
        threshold = initial_avg * 0.75  # 25% under average
        filtered_speeds = [speed for speed in speeds if speed >= threshold]
        
        # Step 3: Compute the new average of the filtered list
        if filtered_speeds:  # Ensure the list is not empty
            self.count_outliers(speeds[-1],threshold)
            return filtered_speeds
        else:
            # This can happen if all values are outliers, it's up to you how to handle it
            self.outlier_count=0
            return speeds
    def remove_temps(self,file_name):
        for temp_vid in os.listdir(self.temp_directory):
            if len(file_name)<=len(temp_vid):
                if temp_vid[:len(file_name)] == file_name:
                    os.remove(os.path.join(self.temp_directory,temp_vid))
                    print(f"removing {temp_vid} from {self.temp_directory}")
    def move_video(self):
        if os.path.exists(self.temp_file_path):
            shutil.move(self.temp_file_path, self.video_directory)
            print(f"moving {self.file_name} from {self.temp_directory} to {self.video_directory}")
            self.remove_temps(self.file_name)
            return True
        if os.path.exists(self.complete_file_path):
            print(f"{self.file_name} already existed in {self.video_directory}; removing it from {self.temp_directory}")
            self.remove_temps(self.file_name)
            return True
        return False
    def yt_dlp_downloader(self,url,ydl_opts={},download=True):
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                self.info_dict=ydl.extract_info(url=url, download=download)
            return True
        except:
            return False
    def progress_callback(self, d):
        self.status_dict = d
        keys = ['status',
                'downloaded_bytes',
                'fragment_index',
                'fragment_count',
                'filename',
                'tmpfilename',
                'max_progress',
                'progress_idx',
                'elapsed',
                'total_bytes_estimate',
                'speed',
                'eta',
                '_eta_str',
                '_speed_str',
                '_percent_str',
                '_total_bytes_str',
                '_total_bytes_estimate_str',
                '_downloaded_bytes_str',
                '_elapsed_str',
                '_default_template']
        if self.status_dict['status'] == 'finished':
            print("Done downloading, moving video to final directory...")
            self.move_video()
            return
        if get_time_stamp()-self.last_checked>5:
            print(self.status_dict['_default_template'])
            self.last_checked = get_time_stamp()
            if (get_time_stamp()-self.start_time/5)>6:
                self.speed_track.append(self.status_dict['speed'])
                self.speed_track=self.filter_outliers(self.speed_track)
                
    def download(self):
        if not os.path.exists(self.video_directory):
            os.makedirs(self.video_directory,exist_ok=True)
        if not os.path.exists(self.temp_directory):
            os.makedirs(self.temp_directory,exist_ok=True)
        for self.num,video_url in enumerate(self.video_urls):
            if video_url != self.video_url or self.video_url == None:
                self.video_url=video_url
                self.info_dict=None
                result = self.yt_dlp_downloader(url=self.video_url,ydl_opts={'quiet': True, 'no_warnings': True},download=False)
                if self.info_dict != None and result:
                    self.start_time = get_time_stamp()
                    self.downloaded = 0
                    self.video_title = self.info_dict.get('title', None)
                    self.video_ext = self.info_dict.get('ext', 'mp4')
                    self.file_name =f"{self.video_title}.{self.video_ext}"
                    self.temp_file_path = os.path.join(self.temp_directory, self.file_name)
                    self.complete_file_path = os.path.join(self.video_directory, self.file_name)
                    if not self.move_video():
                        self.dl_speed = []
                        self.percent=None
                        self.dl_eta=None
                        self.total_bytes_est=None
                        self.percent_speed=None
                        self.speed_track = []
                        self.outlier_count=0
                        ydl_opts = {
                            'outtmpl': self.temp_file_path,
                            'noprogress':True,
                            'progress_hooks': [self.progress_callback]  
                        }
                        
                       
                        print("Starting download...")  # Check if this point in code is reached
                        result = self.yt_dlp_downloader(url=self.video_url,ydl_opts=ydl_opts,download=True)
                        if result:
                            print("Download finished!")  # Check if download completes
                        else:
                            print(f'error downloding {self.video_url}')
                        self.move_video()
                    else:
                        print(f"The video from {self.video_url} already exists in the directory {self.video_directory}. Skipping download.")
                else:
                    print(f"could not find video info from {self.video_url} Skipping download.")
        if self.num==len(self.video_urls)-1:
            self.monitoring=False
            self.time_interval=0
            
    def monitor(self):
        while self.monitoring:
            self.thread_manager.wait(name='pause_event',n=self.time_interval)# check every minute
            if self.monitoring:
                if 'eta' in self.status_dict:
                    if self.outlier_count>=3 and (self.status_dict['eta']/60)>10:
                        self.start()

    def start(self):
        download_thread = self.thread_manager.add_thread(name='download_thread',target=self.download)
        monitor_thread = self.thread_manager.add_thread(name='monitor_thread',target_function=self.monitor)
        self.thread_manager.start(name='download_thread')
        self.thread_manager.start(name='monitor_thread')
        self.thread_manager.join(name='download_thread')
        self.thread_manager.join(name='monitor_thread')
class VideoDownloaderSingleton():
    _instance = None
    @staticmethod
    def get_instance(url_manager,request_manager,title=None,video_extention='mp4',download_directory=os.getcwd(),user_agent=None,download=True,get_info=False):
        if VideoDownloaderSingleton._instance is None:
            VideoDownloaderSingleton._instance = VideoDownloader(url=url,title=title,video_extention=video_extention,download_directory=download_directory,download=download,get_info=get_info,user_agent=user_agent)
        elif VideoDownloaderSingleton._instance.title != title or video_extention != VideoDownloaderSingleton._instance.video_extention or url != VideoDownloaderSingleton._instance.url or download_directory != VideoDownloaderSingleton._instance.download_directory or user_agent != VideoDownloaderSingleton._instance.user_agent:
            VideoDownloaderSingleton._instance = VideoDownloader(url=url,title=title,video_extention=video_extention,download_directory=download_directory,download=download,get_info=get_info,user_agent=user_agent)
        return VideoDownloaderSingleton._instance
