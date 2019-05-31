# XML_JSON_Parse
Dynamic XML_JSON parser to convert XML and JSON files into CSV


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

