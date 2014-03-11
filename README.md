# Sublime Text Minimalistic LaTeX Plugin

This is a bare-bones, minimalistic, trimmed-down, lean LaTeX plugin for Sublime Text 3. The plugin uses `latexmk` to build, so I presume that any platform where this script is available should be supported, although I've only tested on OSX.

## How to Install

````
cd ~/Library/Application Support/Sublime Text 3/Packages
git clone https://github.com/dpo/sublime-minilatex.git minilatex
````

In `Tools>Build System`, make sure that `BuildLaTeXFiles` is selected.

## Everything Should Be a Project

Whether your document has a single or multiple source files, every document should be part of a Sublime project. This allows you to edit a source file that isn't the master source file and still be able to compile the master file with `⌘-B`. The project name should be the same as the master file's base name. For example, if your master file is `mydocument.tex`, the project name should be `mydocument`.

## Command Summary

Function        | Command       | Notes
----------------|---------------|-------------------------
Build           | `⌘-B`         |
Preview PDF     | `⌘-shift-B`   |
List errors     | `alt-shift-L` | (requires [Rubber](https://launchpad.net/rubber))
Clean up        | `alt-shift-C` |
Run BibTeX      | `alt-shift-B` |
Refresh Preview | `alt-shift-P` | (only if not using Skim)
Forward Sync    | `alt-shift-f` | (only if using Skim)

## Navigating LaTeX Errors and Warnings

Currently, the log file is not parsed to facilitate error reporting. However, the Sublime build system is able to recognize errors (to some extent). Once the build is finished, hit `F4`/`shift-F4` to navigate through the error messages.

Optionally, you may install [Rubber](https://launchpad.net/rubber) and hit `alt-shift-L` to display a trimmed-down version of the log. On OSX, if you use [Homebrew](http://brew.sh), it's a simple matter of running
````
brew install rubber
````

Linux users can use [Linuxbrew](https://github.com/Homebrew/linuxbrew).

## Using Preview

By default, `Preview.app` is the PDF previewer. An advantage of Preview is that it ships with OSX. A disadvantage is that it doesn't automatically refresh the display when the PDF file is updated unless you go and click in the Preview window, which is inconvenient. To simulate auto-update, I included the special command `alt-shift-P` (P is for Preview). This command is actually a short AppleScript command that activates the Preview window, causing the PDF to be refreshed, and then switches the focus back to the Sublime Text window. The mechanism is very simplistic for now and is probably easy to fool. However, it's functional.

## Using Skim

You can change the PDF previewer in `BuildLaTeXFiles.sublime-build`. It is currently set to `Preview.app` but you could also use [`Skim.app`](http://skim-app.sourceforge.net). Simply replace the line

    "cmd": ["open", "-a", "Preview.app", "$project_path/$file_base_name.pdf"],

with

    "cmd": ["open", "-a", "Skim.app", "$project_path/$file_base_name.pdf"],

## Companions

* [Sublime BibTeX](https://github.com/dpo/sublime-bibtex): BibTeX snippets

## Customizing

You can customize the `latexmk` options by editing `BuildLaTeXFiles.sublime-build`. However, I recommend creating a `~/.latexmkrc` resource file instead. Here's an example resource file that you can just copy and paste:

````
$pdf_mode = 1;
$pdflatex = 'pdflatex -file-line-error -shell-escape -synctex=1 %O %S';
$pdf_previewer = 'open -a %S';
$pdf_update_method = 0;
$clean_ext = "synctex.gz bbl tdo loa";
$bibtex_use = 2;
````

See the `latexmk` man page for more options.


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/dpo/sublime-minilatex/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

