#!/usr/bin/python3

#Define a variable named ip_target that contains the first 3 octets of a class IP address, /24 CIDR.
ip_response = []
ip_target = '13.224.2.'

#import and use the python subprocess module at the top of your script.
import subprocess

#Write a main function that will be the initial function called by your application.
def main():
#Using a standard for loop and the subprocess.run() method, write a function that loops over all 256 possible IP addresses and does the following:
    #ip_result = subprocess.run(['fping', '13.224.2.0', '-C 5', '-a', '-q'], capture_output=True, text=True)
#Generate all IP address to loop over 256 possible IP's
    for ip in range(1, 5):
        ip_address = ip_target + str(ip)
        ip_result = subprocess.run(['fping', '13.224.2.0', '-C 5', '-a', '-q'], capture_output=True, text=True)
        print(ip_address)
#Call fping on all ipaddress
        ip_list = ip_address
#store results in a list
        ip_response.append(ip_result)


    for ip_output in ip_response:
        #write results to file
        output = ip_output.stderr
        ip_split = output.split(':')
        ip_split_el = ip_split[0]
        ip_split_el2 = ip_split[1]
        print(ip_split_el)
        print(ip_split_el2)
#write input to a .txt file
        text = open('pingsweep-results.txt', 'w')
        text.write('The following hosts were found to be online and responding to ping requests:\n\n')
        text.write('Detected Hosts:\n')
        text.write('==============\n')
        text.write(str(ip_split_el + '\n' + 'Total time to scan took : '))
        text.write(str(ip_split_el2))

if __name__ == '__main__':
    main()

