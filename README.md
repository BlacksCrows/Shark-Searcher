# Shark Looking For Prey


**Takes IP address or IP addresses and runs them thru the ipgeolocation.io API to return Owner and Location**
#### This script was created as part of the Red Siege python challenge https://redsiege.com/python
#### The script leverages the free API from https://api.ipgeolocation.io/. You will need to sigup for a free account to obtain an API key. You must change the portion of the get request in ipgeoloc.py (line 36) to your API key for the script to work. It accepts a single IP address with the -t or --target argument, a list of IPs in a text file with -f or --file argument, a single CIDR block with -c or --cidr argument, or a list of CIDR blocks with the -cf or -cfile argument. Debugging is possible with BURP or ZAp proxies using the -d or --debug argument.

[![Version](https://img.shields.io/badge/version-1.3.3-red.svg)]() [![Python3](https://img.shields.io/badge/python-3.8.5-green.svg)]()
[![GitHub issues](https://img.shields.io/github/issues/BlacksCrows/Shark-Searcher.svg)](https://github.com/BlacksCrows/Shark-Searcher/issues)
[![GitHub forks](https://img.shields.io/github/forks/BlacksCrows/Shark-Searcher.svg)](https://github.com/BlacksCrows/Shark-Searcher/network)
[![GitHub stars](https://img.shields.io/github/stars/BlacksCrows/Shark-Searcher.svg)](https://github.com/BlacksCrows/Shark-Searcher/stargazers)
[![GitHub license](https://img.shields.io/github/license/BlacksCrows/Shark-Searcher.svg)](https://github.com/BlacksCrows/Shark-Searcher/blob/master/LICENSE)

**First you need to install all the dependencies so that the shark starts looking**

#### Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your POST data**
```!pip install requests```

#### Starting with Python 3.3 there's an ipaddress module in the Python standard library which provides layer 3 address manipulation capabilities overlapping**
```!pip install netaddr```
#### The argparse module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv**
```!pip install argparse```

```
              /""-._
             .      '-,
             :         '',
             ;      *     '.
             ' *         () '.
              \               \
               \      _.---.._ '.
                :  .' _.--''-''  \ ,'
  .._            '/.'             . ;
   ; `-.          ,                \'
    ;   `,         ;              ._\
     ;    \     _,-'                ''--._
      :    \_,-'                          '-._
       \ ,-'                       .          '-._
      .'         __.-'';            \...,__       '.
     .'      _,-'       \              \   ''--.,__ '\
    /   _,--' ;          \             ;           "^.}
   ;_,-' )     \  )\      )            ;
        /       \/  \_.,-'             ;
       /                              ;
    ,-'  _,-'''-.    ,-.,            ;
 ,-' _.-'        \  /    |/'-._...--'
:--``             )/
```
