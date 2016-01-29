I write a shell script to indent LaTeX documents with the perl package `[latexindent](https://www.ctan.org/pkg/latexindent)`.

# How to use?

Usage:

```
./latexindent.sh path/filename.tex
```

What the shell script does are:

- generate the indented tex documents which is still named `filename.tex`

- backup the original tex file `filename.tex` as `filename.tex.old`



# The usage of latexindent

```bash
latexindent.pl version 2.1R
usage: latexindent.pl [options] [file][.tex]
      -h  help (see the documentation for detailed instructions and examples)
      -o  output to another file; sample usage
                latexindent.pl -o myfile.tex outputfile.tex
      -w  overwrite the current file- a backup will be made, but still be careful
      -s  silent mode- no output will be given to the terminal
      -t  tracing mode- verbose information given to the log file
      -l  use localSettings.yaml (assuming it exists in the directory of your file)
      -d  ONLY use defaultSettings.yaml, ignore ALL user files
      -c=cruft directory used to specify the location of backup files and indent.log
```

