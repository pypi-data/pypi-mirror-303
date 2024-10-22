# Githubtoolkit
## Usage
### Uploading a file
You can upload a file using<br/>
<code>githubtoolkit.upload_file_to_github(file, repo, token, branch, alias, comment)</code>, where<br/>
#### Required
<li>- <code>file</code> specifies the path to the file you want to load up</li>
<li>- <code>repo</code> specifies the repository you want to upload to</li>
<li>- <code>token</code> is your login method</li>

#### Not required
<li>- <code>branch</code> specifies the branch uploaded to (standard: <code>"main"</code>)</li>
<li>- <code>alias</code> specifies the path the file is uploaded in (standard: <code>file</code>)</li>
<li>- <code>comment</code> adds a comment to your changes (standard: <code>"Update "+filename_</code>)</li>

### Other methods
Also, you can call the <code>main()</code> method to get a uploading agent.<br/>
The <code>about()</code> method returns information about your specific release.

### More coming soon...