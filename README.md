# XML_JSON_Parse
Dynamic XML_JSON parser to transform XML and JSON files to CSV in a instant by the use of multi threading.


<h3>Prerequisities</h3>
<p>The module was developed in python3 with usage of xml, json, pandas, threading, queue module.</p>


<h3>Usage / Start Proces</h3>
<pre>
<h4>For XML parsing</h4>
<code>python3 main.py -i resident.xml -o resident_output.csv -e Resident
</code>
</pre>

<pre>
<h4>For JSON parsing</h4>
<code>python3 main.py -i sample_2.json -o sample_2_output.csv -e fruit
</code>
</pre>

<p><strong>Command Line Arguments:</strong>
  
<h4>usage: main.py [-h] -i INPUT_FILE -o OUTPUT_FILE -e ELEMENT </h4>

Convert XML or JSON file to csv
<ul>
optional arguments:
  <li><strong>-h</strong>, --help            show this help message and exit</li>
  <li><strong>-i</strong> INPUT_FILE, --input_file INPUT_FILE
                        Source XML or JSON file (mandatory)</li>
  <li><strong>-o</strong> OUTPUT_FILE, --output_file OUTPUT_FILE
                        Destination csv file (mandatory)</li>
  <li><strong>-e</strong> ELEMENT, --element ELEMENT
                        element to parse (mandatory)</li>
</ul>
</p>

# Example For XML parsing
<h4> Input xml file : resident.xml with Resident as element to parse</h4>

```python
<State>
<Resident>
<Name>Sample Name</Name>
	<PhoneNumber>1234567891</PhoneNumber>
	<EmailAddress>sample_name@example.com</EmailAddress>
	<Address>
		<StreetLine1>Street Line1</StreetLine1>
		<City>City Name</City>
		<StateCode>AE</StateCode>
		<PostalCode>12345</PostalCode>
	</Address>
</Resident>
<Resident>
	<Name>Sample Name1</Name>
	<PhoneNumber>1234567891</PhoneNumber>
	<EmailAddress>sample_name1@example.com</EmailAddress>
	<Address>
		<StreetLine1>Current Address</StreetLine1>
		<City>Los Angeles</City>
		<StateCode>CA</StateCode>
		<PostalCode>56666</PostalCode>
	</Address>
</Resident>
</State>
```

<code>python3 main.py -i resident.xml -o resident_output.csv -e Resident</code>

<h4> output CSV file : resident_output.csv </h4>

|Resident##Address##City | Resident##Address##PostalCode | Resident##Address##StateCode | Resident##Address##StreetLine1 | Resident##EmailAddress | Resident##Name | Resident##PhoneNumber |
| --- | --- | --- | --- | --- | --- | --- |
|Los Angeles | 56666 | CA | Current Address | sample_name1@example.com | Sample Name1 | 1234567891 |
|City Name | 12345 | AE | Street Line1 | sample_name@example.com | Sample Name | 1234567891 |


# Example For JSON parsing
<h4> Input json file : sample_2.json with fruit as element to parse</h4>

```python
{
    "fruit":[
        {
            "name":"Apple",
            "binomial name":"Malus domestica",
            "major_producers":[
                "China", 
                "United States", 
                "Turkey"
            ],
            "nutrition":{
                "carbohydrates":"13.81g",
                "fat":"0.17g",
                "protein":"0.26g"
            }
        },
        {
            "name":"Orange",
            "binomial name":"Citrus x sinensis",
            "major_producers":[
                "Brazil", 
                "United States", 
                "India"
            ],
            "nutrition":{
                "carbohydrates":"11.75g",
                "fat":"0.12g",
                "protein":"0.94g"
            }
        },
        {
            "name":"Mango",
            "binomial name":"Mangifera indica",
            "major_producers":[
                "India", 
                "China", 
                "Thailand"
            ],
            "nutrition":{
                "carbohydrates":"15g",
                "fat":"0.38g",
                "protein":"0.82g"
            }
        }
    ]
}
```

<code>python3 main.py -i sample_2.json -o sample_2_output.csv -e fruit</code>

<h4> output CSV file : sample_2_output.csv </h4>

|fruit##binomial name | fruit##major_producers | fruit##name | fruit##nutrition##carbohydrates | fruit##nutrition##fat | fruit##nutrition##protein|
| --- | --- | --- | --- | --- | --- |
|Mangifera indica | India&#124;&#124;China&#124;&#124;Thailand | Mango | 15g | 0.38g | 0.82g|
|Citrus x sinensis | Brazil&#124;&#124;United States&#124;&#124;India | Orange | 11.75g | 0.12g | 0.94g|
|Malus domestica | China&#124;&#124;United States&#124;&#124;Turkey | Apple | 13.81g | 0.17g | 0.26g|





