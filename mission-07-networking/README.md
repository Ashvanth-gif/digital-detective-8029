# Mission 7 — How Computers Communicate

## 1. Task / objective
I learned some basic network terms and what happens when I open a website.

## 2. Work completed

### Network terms
- **LAN:** A network in a small area, like a home or school.
- **MAN:** A network that covers a city or large campus.
- **WAN:** A network that covers a large area. The Internet is an example.
- **DNS:** Finds the network address linked to a website name.
- **Router:** Sends data between networks.
- **Protocol:** Rules that devices follow to communicate.
- **Packet switching:** Splits data into small packets that travel across a network.
- **Client-server:** A client asks for something, and a server responds.

### Network checks
I checked whether I could reach `example.com` and looked up its DNS information.

- Connectivity check result: [write what happened; do not include any IP addresses]
- DNS lookup result: [say whether it worked; do not include any IP addresses]

### What happens when I open a website
1. I enter a website address in my browser.
2. DNS helps find the address for the website.
3. My computer sends a request through the network.
4. The website’s server receives the request.
5. The server sends information back.
6. My browser displays the page.

## 3. Commands / tools used
- `ping -c 4 example.com` — checked whether the website responded.
- `nslookup example.com` — checked DNS information.


## 4. My understanding
Devices use networks to send information. DNS helps find websites by name, and a browser uses network requests to get a webpage from a server.

## 5. Difficulties faced
I was unsure how DNS helps my browser find a website.

## 6. How I resolved them
I used a DNS lookup to see that a website name is looked up before the browser can connect to it.

## 7. Evidence / files
I recorded the results of my connectivity check and DNS lookup. I removed any IP addresses and personal network information.

## 8. Commit details
Commit message: `Explain networking concepts and website communication`
Status: Committed and pushed.