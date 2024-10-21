% ------------------------------------------------------------------------------
% SPDX-License-Identifier: CC-BY-4.0
% Copyright (C) 2024 Jayesh Badwaik <j.badwaik@fz-juelich.de>
% ------------------------------------------------------------------------------
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{jureap}
\LoadClassWithOptions{scrartcl}

%--------------------------------------------------------------------------------------------------
% Language and Font Support
% --------------------------------------------------------------------------------------------------
\RequirePackage{fontspec}
\RequirePackage{microtype}
\PassOptionsToPackage{final}{microtype}
\RequirePackage{unicode-math}

\setmainfont[Ligatures=TeXOff,ItalicFont={Linux Libertine O Italic}]{Alegreya}
\setsansfont{Alegreya Sans}
%\setmathfont[math-style=upright,Scale=MatchLowercase]{Latin Modern Math}
\setmathfont[Scale=MatchLowercase]{Latin Modern Math}

\setmathfont[range={bb},Scale=MatchLowercase]{TeX Gyre Pagella Math}
\setmathfont[range={scr,bfscr},Scale=MatchLowercase]{Tex Gyre Bonum Math}
\setmathfont[range=\setminus,Scale=MatchLowercase]{XITS Math}
\linespread{1.2}

\RequirePackage{polyglossia}
\setmainlanguage{english}
\RequirePackage{csquotes}

% --------------------------------------------------------------------------------------------------
% Color Support for the Document
% --------------------------------------------------------------------------------------------------
\RequirePackage[usenames,dvipsnames,svgnames,table]{xcolor}

% --------------------------------------------------------------------------------------------------
% Hyperref Support with Colored Links
% --------------------------------------------------------------------------------------------------
\RequirePackage{hyperref}
\PassOptionsToPackage{hypertexnames=true,plainpages=false,pdfpagelabels,pagebackref}{hyperref}

\RequirePackage{cleveref}
\PassOptionsToPackage{capitalize,nameinlink}{cleveref}

\providecommand{\penchurlcolor}{Sepia}
\providecommand{\penchlinkcolor}{MidnightBlue}
\providecommand{\penchcitecolor}{ForestGreen}

\RequirePackage{hyperxmp}
\hypersetup{
  keeppdfinfo,colorlinks=true,
  urlcolor=\penchurlcolor, linkcolor=\penchlinkcolor, citecolor=\penchcitecolor,
  pdftitle={\@title}, pdfauthor={\@author}, pdfsubject={\@subject}
}

% --------------------------------------------------------------------------------------------------
%  BibTeX Support
% --------------------------------------------------------------------------------------------------
\RequirePackage[
sortcites = true,
sorting=nyt,
bibstyle=alphabetic,
citestyle=alphabetic,
backend=biber
]{biblatex}



% --------------------------------------------------------------------------------------------------
% Configure ToC Tools
% --------------------------------------------------------------------------------------------------
\PassOptionsToClass{headings=optiontoheadandtoc}{scrartcl}
\setcounter{secnumdepth}{3}
\setcounter{tocdepth}{2}

\RedeclareSectionCommand[tocnumwidth=2.0em]{part}
\RedeclareSectionCommand[tocindent=1.0em,tocnumwidth=2.0em]{section}
\RedeclareSectionCommand[tocindent=2.5em,tocnumwidth=2.5em]{subsection}

% --------------------------------------------------------------------------------------------------
% Configure Headers
% --------------------------------------------------------------------------------------------------
\RequirePackage[automark,autooneside=false]{scrlayer-scrpage}
\defpairofpagestyles{title}{
  \clearpairofpagestyles
  \cfoot{\rule[\baselineskip]{\textwidth}{0.1pt}}
  \ofoot{\pagemark}
}

\defpairofpagestyles{main}{
  \clearpairofpagestyles
  \cfoot{\rule[\baselineskip]{\textwidth}{0.1pt}}
  \chead{\rule[-\baselineskip]{\textwidth}{0.1pt}}
  \automark[subsection]{section}
  \ofoot{\pagemark}
  \ihead{\leftmark}
  \ohead{\Ifstr{\leftmark}{\rightmark}{}{\rightmark}}
}

\renewcommand*{\titlepagestyle}{title}

% --------------------------------------------------------------------------------------------------
% Configure Part Titles to be on a Separate Page
% --------------------------------------------------------------------------------------------------
\renewcommand\partheadstartvskip{\clearpage\null\vfil}
\renewcommand\partheadmidvskip{\par\nobreak\vskip 20pt\thispagestyle{empty}}
\renewcommand\partheadendvskip{\vfil\clearpage}
\renewcommand\raggedpart{\centering}


% --------------------------------------------------------------------------------------------------
% Misc Tools
% --------------------------------------------------------------------------------------------------
\RequirePackage{setspace}
\RequirePackage{enumitem}
\RequirePackage{graphicx}
\RequirePackage{csvsimple}
\RequirePackage{listings}
\RequirePackage{multicol}
\RequirePackage{subcaption}
\RequirePackage{float}
\RequirePackage{booktabs}


\lstset{
  basicstyle=\footnotesize,        % the size of the fonts that are used for the code
  captionpos=b,                    % sets the caption-position to bottom
  breaklines=true,
  postbreak=\mbox{\textcolor{red}{$\hookrightarrow$}\space}
}


\makeatletter
\csvset{
  autotabularcenter/.style={
    file=#1,
    after head=\csv@pretable\begin{tabular}{|*{\csv@columncount}{c|}}\csv@tablehead,
    table head=\hline\csvlinetotablerow\\\hline,
    late after line=\\,
    table foot=\\\hline,
    late after last line=\csv@tablefoot\end{tabular}\csv@posttable,
    command=\csvlinetotablerow},
}
\makeatother
\newcommand{\csvautotabularcenter}[2][]{\csvloop{autotabularcenter={#2},#1}}

% --------------------------------------------------------------------------------------------------
% Section Title Formatting
% --------------------------------------------------------------------------------------------------

\RequirePackage{relsize}
\RequirePackage{ifthen}

% Set Font Size of Section Title Text
\addtokomafont{section}{\fontsize{2ex}{2ex}\selectfont}

% Set font size of Section Number Text
\newkomafont{sectionnumber}{\fontsize{3ex}{3ex}\selectfont\rmfamily}

% Format for Section Number
\renewcommand\sectionformat{\usekomafont{sectionnumber}{\thesection\autodot}\quad}

% Format for Displaying the Section/Subsection Title
\makeatletter
\renewcommand\sectionlinesformat[4]{
  \ifthenelse{
    \equal{\detokenize{#1}}{\detokenize{section}}
  }{
    \makebox[1em][l]{\rule[-1ex]{\textwidth}{1pt}}
  }{
  }
  \@hangfrom{\hskip #2#3}{#4}
}
\makeatother

% --------------------------------------------------------------------------------------------------
% Commands for Artifacts
% --------------------------------------------------------------------------------------------------

\lstset{mathescape=true}

\newcommand{\exacbplot}[1]{
  \begin{figure}[H]
    \begin{center}
      \includegraphics[width=0.8\textwidth]{#1}
    \end{center}
  \end{figure}
}

\newcommand{\exacbtable}[2]{
\begin{table}[H]
\resizebox{\textwidth}{!}{
  \csvautotabularcenter[respect underscore=true]{#1}
}
\caption{#2}
\end{table}
}


