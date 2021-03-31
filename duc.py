
'''
Source: duc.py
Author: udpdm1
duc.py is a simple python3 script to interact with domains.google.com to update a synthetic DNS record of the type of DDNS for changing addresses. 
Google documentation page: https://support.google.com/domains/answer/6147083?hl=en#zippy=%2Cusing-the-api-to-update-your-dynamic-dns-record
Google DDNS API: https://domains.google.com/nic/update
duc.py uses a duc.conf file in the same directory as the duc.py script to input the google domains specific parameters.
duc.conf file contents should look as below with your own values for hostname, username, password populated:

[duc-config]
hostname="myhost.mydomain.tld"
username="myusername"
password="mypassword"

'''

import configparser                     #used to help read a configuration file
import socket                           #used to access the host TCP/IP address
import requests                         #used to help for the POST web call against Google's DDNS API



#Returns TCP/IP address of local machine
#Note that the code will likely have trouble if you have multiple IPs / interfaces
#
def get_host_name_ip(): 
    try:
       print("Now getting host_name and host_ip info...")
       name = socket.gethostname().lower()
       ip = socket.gethostbyname(name)
       return (ip)
       
    except:
       print("Unable to get Hostname and IP")



#Get configuration data file here (duc.conf)
def get_conf(): 
  config = configparser.RawConfigParser()   
  configfilepath = r'c:\tools\duc\duc.conf'
  config.read(configfilepath)
  myhost=config.get('duc-config','hostname')
  myuser=config.get('duc-config','username')
  mypass=config.get('duc-config','password')
  
  return myhost, myuser, mypass



#Will update google domain using information from config file and current IP address
def set_ddns(myhost, myuser, mypass, host_ip): 
  '''
  The API requires HTTPS. Here’s an example request:
  https://username:password@domains.google.com/nic/update?hostname=subdomain.yourdomain.com&myip=1.2.3.4
  Note: You must set a user agent in your request as well. Web browsers will generally add this for you when testing via the above url. In any case, the final HTTP request sent to our servers should look something like this:
  Example HTTP query:
  POST /nic/update?hostname=subdomain.yourdomain.com&myip=1.2.3.4 HTTP/1.1
  Host: domains.google.com
  Authorization: Basic base64-encoded-auth-string User-Agent: Chrome/41.0 your_email@yourdomain.com
  '''
  myurl = "https://" + myuser +":" + mypass + "@domains.google.com/nic/update?hostname=" + myhost + "&myip=" + host_ip
 
  result = requests.post(myurl)

  return result, result.url, result.text



def main():
  #MAIN section

  #Get the TCP/IP address currently associated with this machine (assumes there is only one)
  host_ip = get_host_name_ip() 

  #Read config settings for DNS host record to update and google domains username and password to authenticate for the google domains sythentic record from the duc.conf file.
  myhost, myuser, mypass = get_conf() 

  #Attempt to set the DDNS IP address value in google domains using Google's DDNS API interface over HTTPS.
  myresults=set_ddns(myhost.strip('"'), myuser.strip('"'), mypass.strip('"'), host_ip.strip('"')) 

  print(f'We have made it to the end: myhost: {myhost} myuser: {myuser} mypass: {mypass}')
  print(f'result:      {myresults[0]}')
  print(f'result.url:  {myresults[1]}')
  print(f'result.text: {myresults[2]}')


if __name__ == '__main__':
  main()

 