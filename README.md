# Sublime Minimalistic LaTeX Plugin

This is a bare-bones, minimalistic, trimmed-down, lean LaTeX plugin for Sublime Text 3. It doesn't parse the log file. It doesn't provide LaTeX snippets or reference/citation completion.

In order to use this plugin, clone this repository in your `~/Library/Application Support/Sublime Text 3/Packages`. In `Tools>Build System`, make sure that `BuildLaTeXFiles` is selected.

## Usage

Function        | Command
----------------|--------------
Build           | `⌘-B`
Preview PDF     | `⌘-shift-B`
Clean up        | `alt-shift-C`
Run BibTeX      | `alt-shift-B`
Refresh Preview | `alt-shift-P`

## Everything Should Be a Project

Whether your document has a single or multiple source files, every document should be part of a Sublime project. This allows you to edit a source file that isn't the master source file and still be able to compile the master file with `⌘-B`. The project name should be the same as the master file's base name. For example, if your master file is `mydocument.tex`, the project name should be `mydocument`.

## Using Preview

By default, `Preview.app` is the PDF previewer. An advantage of Preview is that it ships with OSX. A disadvantage is that it doesn't automatically refresh the display when the PDF file is updated unless you go and click in the Preview window, which is inconvenient. To simulate auto-update, I included the special command `alt-shift-P` (P is for Preview). This command is actually a short AppleScript command that activates the Preview window, causing the PDF to be refreshed, and then switches the focus back to the Sublime Text window. The mechanism is very simplistic for now and is probably easy to fool. However, it's functional.

## Using Skim

You can change the PDF previewer in `BuildLaTeXFiles.sublime-build`. It is currently set to `Preview.app` but you could also use [`Skim.app`](http://skim-app.sourceforge.net). Simply replace the line

    "cmd": ["open", "-a", "Preview.app", "$project_path/$file_base_name.pdf"],

with

    "cmd": ["open", "-a", "Skim.app", "$project_path/$file_base_name.pdf"],

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
