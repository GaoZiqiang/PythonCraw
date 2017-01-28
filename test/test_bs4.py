
from bs4 import BeautifulSoup
import re

html_doc = """
<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE html
        PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml"
    xmlns:h="http://java.sun.com/jsf/html"
    xmlns:f="http://java.sun.com/jsf/core">
<h:head>
    <title>314 LabManagement Technology</title>
    <!-- css style partly from: http://www.coreservlets.com/JSF-Tutorial/jsf2 -->
    <link href="css/styles.css" rel="stylesheet" type="text/css" />
    <link href="css/table-styles.css" rel="stylesheet" type="text/css" />
    <link href="css/style.css" rel="stylesheet" type="text/css" />
</h:head>
<h:body id="body">
    <div class="container">
        <div id="header">
            <h1>lll</h1>
        </div>
        <ul id="nav">
            <li><a href="./index.jsf">fasg</a></li>
            <li><a href="./returning.jsf">faga</a></li>
            <li><a href="./lending.jsf">hsre</a></li>
            <li><h:link outcome="storage.jsf" rendered="#{login.root}">heh</h:link></li>
            <li><h:link outcome="report.jsf" rendered="#{login.root}">jet</h:link></li>
            <li><a href="./aboutus.jsf">hj</a></li>

        </ul>
        <div class="right">
            <div id="daohang">

                <ul>

                    <li><a href="#">jym</a></li>

                    <li><a href="#">mmy</a></li>

                    <li><a href="#">theh</a></li>

                    <li><a href="#">ns</a></li>
                    
                    <li><a href="#">mjj</a></li>

                    <li><a href="#">kuu</a></li>

                    <li><a href="./login.jsf">grtjhtrj</a></li>

                </ul>

            </div>


            <div id="section">
            </div>
        </div>
        <div id="footer">copyright@ 314softlab.com</div>
    </div>
</h:body>
</html>
 """
 
soup = BeautifulSoup(html_doc,'html.parser',from_encoding='uft-8')

print '------find all links------'

links = soup.find_all('a')
for link in links:
    print link.name,link['href'],link.get_text()


print '------find one node------'
link_node = soup.find('a',href = './returning.jsf')

print link_node.name,link_node['href'],link_node.get_text()


print '------ZhengZ1eBiaoDaShi------'
link_nodes= soup.find('a',href = re.compile(r"ret"))
print link_nodes.name,link_nodes['href'],link_nodes.get_text()

