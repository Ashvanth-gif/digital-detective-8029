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
I checked whether I could reach GitHub at `github.com` and looked up its DNS information.

- Connectivity check: `ping -c 4 github.com` received all 4 replies with no packet loss.
- DNS lookup: `nslookup github.com` succeeded and returned an address record. I have not included the IP address.

### Task 7.2 questions
- **What does a connectivity test check?** It checks whether my computer can send data to a website and receive a reply.
- **What information does a DNS lookup display?** It shows DNS records for a domain, such as the network addresses associated with its name. I left the actual addresses out of my notes.
- **What does DNS do when I enter a website name?** DNS looks up the network address for that name so the browser can contact the website's server.

### What happens when I open a website
1. I enter a website address in my browser.
2. DNS helps find the address for the website.
3. My computer sends a request through the network.
4. The website’s server receives the request.
5. The server sends information back.
6. My browser displays the page.

## 3. Commands / tools used
- `ping -c 4 github.com` — checked whether the website responded.
- `nslookup github.com` — checked DNS information.


## 4. My understanding
Devices use networks to send information. DNS helps find websites by name, and a browser uses network requests to get a webpage from a server.

## 5. Difficulties faced
I was unsure how DNS helps my browser find a website.

## 6. How I resolved them
I used a DNS lookup to see that a website name is looked up before the browser can connect to it.

## 7. Evidence / files
The privacy-safe results are recorded in [`evidence/mission-07-networking.txt`](../evidence/mission-07-networking.txt). The note leaves out IP addresses and personal network information.

## 8. Commit details
Commit message: `Document GitHub network lookup results`
Status: Committed and pushed.
