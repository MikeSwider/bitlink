# bitlink
A sublime extention that opens your current file in bitbucket. 

## Installation
Download this package and move the files into:

```/Library/Application Support/Sublime Text 3/Packages```

Open `bitlink.sublime-settings` and set your remote

```
{
	"remote": "http://bitbucket.com/{{username}}/{{repo}}"
}
```

## Usage 
Right click from within a file and select bitlink

Open - Opens the file at the current line number your default web browser

Copy - Copies the url of the current file and line number. To be pasted in slack or email

Blame - Opens the file at the current line number with blame. 
