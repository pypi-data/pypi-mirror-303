# Githubtoolkit
A Python module for interacting with GitHub
## Installation
### Using *pip*
You can install githubtoolkit via pip using
<li>in a commandline:</li><br/>

```
py -m pip install githubtoolkit
```
<li>in a python script:</li><br/>

```python
import os
os.system('py -m pip install githubtoolkit')
```

## Usage
### Uploading a file
You can upload a file using<br/>

```python
githubtoolkit.upload_file_to_github(file, repo, token, branch, alias, comment)
```

#### Required
<li><code>file</code> specifies the path to the file you want to load up</li>
<li><code>repo</code> specifies the repository you want to upload to</li>
<li><code>token</code> is your login method</li>

#### Not required
<li><code>branch</code> specifies the branch uploaded to (standard: <code>"main"</code>)</li>
<li><code>alias</code> specifies the path the file is uploaded in (standard: <code>file</code>)</li>
<li><code>comment</code> adds a comment to your changes (standard: <code>"Update "+filename_</code>)</li>

### Uploading file content directly
You can also directly upload the content of a file instead of letting the program do that.<br/>
Therefore, you can use
```python
githubtoolkit.upload_content_to_github(content, file_path, repo, token, branch, comment)
```
<br/>
None of these args have default values as they are normally called by the above function.<br/><br/>
The values that aren't explained above are:<br/>
<li><code>content</code> is the content of the file</li><br/>
<li><code>file_path</code> is now used as the path your file is saved under on GitHub</li>

### Other methods
Also, you can call the <code>main()</code> method to get a uploading agent.<br/>
The <code>about()</code> method returns information about your specific release.<br/><br/>
You can call the main function from a commandline using
```
py -m githubtools
```

### Contact
Use the following for contact / feedback information:
```python
githubtools.about()["feedbackTo"]
```

### Credits
This module is a fork of <code>upload-content-to-github</code>.<br/>
This means some of the credits go to <code>bohachu</code>.

### More coming soon...