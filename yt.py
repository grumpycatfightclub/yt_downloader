import pytube

def download_video(url, resolution):
    url = input_url()
    resolution = choose_resolution()
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(resolution)
    print("downloading...")
    stream.download()
    print("downloaded!")
    return stream.default_filename

def download_videos(url, resolution):
    urls = input_url()
    resolution = choose_resolution()
    for url in urls:
        download_video(url, resolution)

def download_playlist(url, resolution):
    url = input_url()
    resolution = choose_resolution()
    playlist = pytube.Playlist(url)
    download_videos(playlist.video_urls, resolution)

def choose_resolution():
    print("\t\t\tRESOLUTIONS\n\t[Type 'low' or '360' or '360p' --> 360p],\n\t[Type 'medium' or '720' or '720p' or 'hd' --> 720p]\n\t[Type 'high' or '1080' or '1080p' or 'fullhd' or 'full_hd' or 'full hd' --> 1080p]\n\t[Type 'very high' or '2160' or '2160p' or'4K' or'4k' --> 4K]")
    resolution = input("\t:")
    if resolution in ["low", "360", "360p"]:
        itag = 18
    elif resolution in ["medium", "720", "720p", "hd"]:
        itag = 22
    elif resolution in ["high", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
        itag = 137
    elif resolution in ["very high", "2160", "2160p", "4K", "4k"]:
        itag = 313
    else:
        itag = 18
    return itag


def input_url():
    print("\tEnter the links of the videos:\n\t:")
    link = input("\t:")
    return link

while True:
    print("\t\t\tYOUTUBE DOWNLOADER\n\tPress 1 --> Download video\n\tPress 2 --> Download playlist\n\tPress 3--> exit")
    entry = int(input('\n\t:'))
    if entry == 1:
        download_video(None, None)
    elif entry == 2:
        download_playlist(None,None)
    elif entry == 3:
        break 
    else:
        continue       
