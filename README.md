# Sublime Minimalistic LaTeX Plugin

This is a bare-bones, minimalistic, trimmed-down, lean LaTeX plugin for Sublime Text 3. It doesn't parse the log file. It doesn't provide LaTeX snippets or reference/citation completion.

In order to use this plugin, clone this repository in your `~/Library/Application Support/Sublime Text 3/Packages`. In `Tools>Build System`, make sure that `BuildLaTeXFiles` is selected.

## Usage

* Building: `⌘-B`
* Previewing PDF: `⌘-shift-B`
* Cleaning up: `alt-shift-C`

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

You can also customize the PDF previewer in `BuildLaTeXFiles.sublime-build`. It is currently set to `Preview.app` but you could also use [`Skim.app`](http://skim-app.sourceforge.net).
