#Instagram DP and Photo Downloader
#Created by Aswin ks
import instaloader

ig=instaloader.Instaloader()


dp = input("Enter the username: ")


ig.download_profile(dp,profile_pic_only=True)
print("Image Saved!")








