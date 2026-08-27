\LoadClass{IEEEtran}

\RequirePackage{ifpdf}
\RequirePackage{xkeyval}

\ifpdf
 \pdfmapfile{+ t1-times.map}
 \pdfmapfile{+ t1-formata.map}
 \pdfmapfile{+ t1-giovannistd.map}
\fi

\newif\iflineno\linenofalse
\newif\ifjtehm\jtehmfalse
\newif\ifaccesseditors\accesseditorsfalse
\newif\ifaccesseditorial\accesseditorialfalse
\newif\ifjtehmeditorial\jtehmeditorialfalse


\newif\ifeoddefined\eoddefinedfalse

\DeclareOption{a4paper}{\setlength{\paperheight}{276.2mm}%
                        \setlength{\paperwidth}{203.2mm}%
                        \@IEEEusingAfourpapertrue}


\DeclareOption{accesseditors}{\accesseditorstrue}

\DeclareOption{editorial}{\accesseditorialtrue\accesseditorstrue\jtehmeditorialtrue}

\DeclareOption{lineno}{\linenotrue}

\DeclareOption{nolineno}{\linenofalse}

\DeclareOption{twoside}{\global\@twosidetrue \@mparswitchtrue}

\DeclareOption{jtehm}{\global\jtehmtrue}

%%%%
\newdimen\@draftversionrule\@draftversionrule0pt %%%%% updated
\DeclareOption{draftversion}{\setlength\overfullrule{5pt}\@draftversiontrue\@draftversionrule.1pt\overfullrule 5pt} %%%%% updated
%%%%

% default to US a4paper, 10pt, twocolumn, twosided, final, journal
\ExecuteOptions{a4paper,10pt,twocolumn,twoside,lineno,journal}
% overrride these defaults per user requests
\ProcessOptions

\ifaccesseditorial
\ifjtehmeditorial\else
  \RequirePackage{ltxutil,ltxgrid}
\fi
\fi

\def\putfont#1#2#3#4#5#6{\usefont{#1}{#2}{#3}{#4}\fontsize{#5}{#6}\selectfont}

\def\textit#1{{\it #1}}%
\def\textbf#1{{\bf #1}}%
\def\historyfont{\sffamily\fontencoding{T1}\fontseries{n}\fontshape{n}\fontsize{7}{8.4}\selectfont}%formata reg 7pt
\def\doifont{\rmfamily\fontencoding{T1}\fontseries{n}\fontsize{6}{7.2}\selectfont\it}%giovannistd-bookitalic 6pt
\def\titlefont{\sffamily\fontencoding{T1}\fontseries{b}\fontsize{22}{25.4}\selectfont}%formata condmed 22pt
\def\authorfont{\sffamily\fontencoding{T1}\fontseries{b}\fontsize{9.9}{12}\selectfont}%formata medium 9.9pt
\def\membershipfont{\sffamily\fontencoding{T1}\fontseries{b}\fontsize{9.9}{12}\selectfont}%formata medium italic 9.9pt
\def\addressfont{\rmfamily\fontencoding{T1}\fontseries{n}\fontsize{6.6}{8}\selectfont}%times roman 6.6pt
\def\correspfont{\rmfamily\fontencoding{T1}\fontseries{n}\fontsize{7.7}{9.24}\selectfont}%times roman 7.7pt
\def\tfootnotefont{\rmfamily\fontencoding{T1}\fontseries{n}\fontsize{7.7}{9.24}\selectfont}%times roman 7.7pt
\def\abstractfont{\rmfamily\fontencoding{T1}\fontseries{n}\fontsize{10}{12}\selectfont}%times roman 10pt
\def\indexfont{\rmfamily\fontencoding{T1}\fontseries{n}\fontsize{10}{12}\selectfont}%times roman 10pt
\def\bodyfont{\rmfamily\fontencoding{T1}\fontseries{n}\fontsize{10}{12}\selectfont}%times roman 10pt
\def\abstractheadfont{\sffamily\fontencoding{T1}\fontseries{b}\fontsize{10}{12}\selectfont}%formata bold 9pt
\def\indexheadfont{\sffamily\fontencoding{T1}\fontseries{b}\fontsize{10}{12}\selectfont}%formata bold 9pt
\def\sectionAfont{\sffamily\fontencoding{T1}\fontseries{b}\fontsize{9}{12}\selectfont}%formata bold 9pt
\def\sectionBfont{\sffamily\fontencoding{T1}\fontseries{b}\fontshape{sl}\fontsize{9}{12}\selectfont}%formata mediumitalic 9pt
\def\sectionCfont{\sffamily\fontencoding{T1}\fontseries{n}\fontsize{9}{12}\selectfont}%formata regular 9pt
\def\sectionDfont{\sffamily\fontencoding{T1}\fontseries{n}\fontshape{sl}\fontsize{9}{12}\selectfont}%formata italic 9pt
\def\figcapheadfont{\sffamily\fontencoding{T1}\fontseries{b}\fontsize{7}{8.4}\selectfont}%formata bold 7pt
\def\figcapfont{\def\textit##1{{\sffamily\selectfont\itshape##1}}\sffamily\fontencoding{T1}\fontseries{m}\fontsize{7}{8.4}\selectfont      }%formata medium 7pt
\def\tablecapheadfont{\sffamily\fontencoding{T1}\fontseries{b}\fontsize{7}{8.4}\selectfont}%formata bold 7pt
\def\tableheadfont{\sffamily\fontencoding{T1}\fontseries{m}\fontsize{7}{8.4}\selectfont}%formata medium 7pt
\def\tablecapfont{\def\textit##1{{\sffamily\selectfont\itshape##1}}\sffamily\fontencoding{T1}\fontseries{m}\fontsize{7}{8.4}\selectfont}%formata medium 7pt
\def\tablebodyfont{\def\textit##1{{\sffamily\selectfont\itshape##1}}\sffamily\fontencoding{T1}\fontseries{n}\fontsize{7}{8.4}\selectfont}%formata regular 7 pt
\def\tablefootfont{\sffamily\fontencoding{T1}\fontseries{b}\fontsize{7}{8.4}\selectfont}%formata regular 7 pt
\def\footervolfont{\sffamily\fontencoding{T1}\fontseries{n}\fontsize{6}{7}\selectfont}%formata regular 6pt
\def\footerpagefont{\sffamily\fontencoding{T1}\fontseries{n}\fontsize{7}{7}\selectfont}%formata regular 7pt
\def\headerfont{\sffamily\fontencoding{T1}\fontseries{n}\fontsize{7}{7}\selectfont}%formata regular 7pt
\def\nheaderfont{\sffamily\fontencoding{T1}\fontseries{b}\fontsize{9}{9}\selectfont}%formata regular 7pt
\def\iheaderfont{\sffamily\fontencoding{T1}\fontseries{m}\fontshape{sl}\fontsize{7}{7}\selectfont}%formata mediumitalic 9pt
\def\referencefont{\rmfamily\fontencoding{T1}\fontseries{n}\fontsize{7.61}{9}\selectfont}%times roman 7.61pt
\def\biographyheadfont{\sffamily\fontencoding{T1}\fontseries{m}\fontsize{8}{9.6}\selectfont}%times roman 8pt
\def\biographyfont{\rmfamily\fontencoding{T1}\fontseries{n}\fontsize{8}{9.6}\selectfont}%times roman 8pt

\ifjtehm
\def\correspfont{\sffamily\fontencoding{T1}\fontseries{n}\fontsize{7}{8}\selectfont}%times roman 7.7pt
\def\tfootnotefont{\sffamily\fontencoding{T1}\fontseries{n}\fontsize{7}{8}\selectfont}%times roman 7.7pt
\def\abstractheadfont{\sffamily\fontencoding{T1}\fontseries{b}\fontsize{9}{12}\selectfont}%formata bold 9pt
\def\indexheadfont{\sffamily\fontencoding{T1}\fontseries{b}\fontsize{9}{12}\selectfont}%formata bold 9pt
\def\titlepageheaderfont{\sffamily\fontencoding{T1}\fontseries{b}\fontsize{9}{12}\selectfont}%formata bold 9pt
\fi

\AtBeginDocument{%
%
%
% enable Times now - so that all class options can see the correct font families
\fontencoding{T1}\selectfont%
\bodyfont\selectfont%
%\advance\baselineskip by 1pt plus 1pt minus 1pt%
}

\columnsep 6.95mm
\columnwidth 85.29mm
\textwidth 177.53mm
%\textheight 236.23mm
\textheight 672pt
\oddsidemargin=12.76mm
\advance\oddsidemargin by -1in
\evensidemargin=12.76mm
\advance\evensidemargin by -1in
\headsep 0.25in
\advance\headsep by 2.8mm

%Defining Pantone SpotColor for blue
\RequirePackage{color}
\ifjtehm
  \definecolor{accessblue}{cmyk}{.24,1,1,0}
  \definecolor{greycolor}{cmyk}{0,0,0,1}
\else
  \RequirePackage{spotcolor}
  \NewSpotColorSpace{PANTONE}
  \AddSpotColor{PANTONE} {PANTONE3015C} {PANTONE\SpotSpace 3015\SpotSpace C} {1 0.3 0 0.2}
  \SetPageColorSpace{PANTONE}%
  \definecolor{accessblue}{spotcolor}{PANTONE3015C,1.0}%
  \definecolor{greycolor}{cmyk}{0,0,0,.8}
\fi
\definecolor{grey}{cmyk}{0,0,0,.1}
\definecolor{black}{cmyk}{0,0,0,1}


%%%
% Page dimensions
%sections
%\def\@seccntformat#1{\csname the#1dis\endcsname\hskip 0.5em\relax}
\def\restoreSection{%
\def\theparagraphdis{\alph{paragraph}:}            % d)
\def\section{\@startsection{section}{1}{1pt}{-1pc plus -1pt minus -1pt}%
              {0.001pt}{\raggedright\color{accessblue}\sectionAfont\uppercase}}%
\def\subsection{\@startsection{subsection}{2}{1pt}{-1pc plus -1pt minus -1pt}%
              {1pt}{\raggedright\color{greycolor}\sectionBfont\uppercase}}%
\def\subsubsection{\@startsection{subsubsection}{3}{1pt}{-1pc plus -1pt minus -1pt}%
              {1pt}{\raggedright\color{greycolor}\sectionCfont\hspace*{-1pt}}}%
\def\paragraph{\@startsection{paragraph}{4}{1pt}{-1pc plus -1pt minus -1pt}%
              {1pt}{\raggedright\color{greycolor}\sectionDfont}}%
}
\restoreSection%
\def\@IEEEprocessthesectionargument#1{%
\@ifmtarg{#1}{%
\section*{{\color{accessblue}\sectionAfont APPENDIX \thesectiondis}}%
\addcontentsline{toc}{section}{Appendix \thesection}}{%
\section*{{\color{accessblue}\sectionAfont APPENDIX \thesectiondis \\* #1}}%
\addcontentsline{toc}{section}{Appendix \thesection: #1}}}

\renewcommand{\appendix}[1][]{\par%
    \def\theHsection{Appendix.A}%
    \xdef\Hy@chapapp{appendix}%
    \setcounter{section}{0}%
    \setcounter{subsection}{0}%
    \setcounter{subsubsection}{0}%
    \setcounter{paragraph}{0}%
    \def\thesection{}%
    \def\thesectiondis{APPENDIX.}% 
    \def\thesubsection{\Alph{subsection}}%
    \refstepcounter{section}%
}

\def\appendices{\par%
    \def\theHsection{Appendix.\Alph{section}}%
    \xdef\Hy@chapapp{appendix}%
    \setcounter{section}{-1}%
    \setcounter{subsection}{0}%
    \setcounter{subsubsection}{0}%
    \setcounter{paragraph}{0}%
    \def\thesection{\Alph{section}}%
    \def\thesectiondis{APPENDIX \Alph{section}}.%
    \refstepcounter{section}%
    \setcounter{section}{0}%
}


%%%
%Captions
\def\@IEEEtablestring{table}

\long\def\@makecaption#1#2{%
\ifx\@captype\@IEEEtablestring%
\begin{flushleft}
\vspace*{5pt}
{\vss\color{accessblue}\tablecapheadfont #1. \ }{\raggedright\tablecapfont#2\vss}%
\end{flushleft}
\@IEEEtablecaptionsepspace%
\else
\@IEEEfigurecaptionsepspace%
\setbox\@tempboxa\hbox{\strut{\color{accessblue}\figcapheadfont #1. \ }\raggedright\figcapfont#2\strut}%
\ifdim \xfigwd >\columnwidth%
\setbox\@tempboxa\hbox{{\color{accessblue}\figcapheadfont #1. \ }}%
\mbox{}\hfill\begin{tabular}{@{}l@{}}\noindent\raggedright\unhbox\@tempboxa\figcapfont#2\end{tabular}\hfill\mbox{}%
\else%
\setbox\@tempboxa\hbox{{\color{accessblue}\figcapheadfont #1. \ }}%
{\vss\raggedright\noindent\unhbox\@tempboxa\figcapfont#2\vss}%
\fi\fi\vskip 1pt plus 1pt minus 1pt}

%tables
\ifjtehm
  \def\thetable{\@Roman\c@table}
\else
  \def\thetable{\@arabic\c@table}
\fi
\def\fps@table{tbp}
\def\ftype@table{2}
\def\ext@table{lot}
\def\tablename{TABLE}
\def\fnum@table{\tablename~\thetable}

%%%
%figures
\def\thefigure{\@arabic\c@figure}
\def\fps@figure{tbp}
\def\ftype@figure{1}
\def\ext@figure{lof}
\def\figurename{FIGURE}
\def\fnum@figure{\figurename~\thefigure}

\define@key{figkeys}{topskip}{\def\fig@topskip{#1}}
\define@key{figkeys}{midskip}{\def\fig@midskip{#1}}
\define@key{figkeys}{botskip}{\def\fig@botskip{#1}}
\setkeys{figkeys}{topskip=0pt,midskip=0pt,botskip=0pt}%

\newsavebox\figbox
\def\Figure{\@ifnextchar[{\@Figure}{\@Figure[t!]}}
\def\@Figure[#1]{\@ifnextchar({\@@Figure[#1]}{\@@Figure[#1](topskip=0pt)}}
\def\@@Figure[#1](#2){\@ifnextchar[{\@@@Figure[#1](#2)}{\@@@Figure[#1](#2)[scale=1]}}
%%%%%%%%%%%%
\def\@@@Figure[#1](#2)[#3]#4#5{%
      \setkeys{figkeys}{#2}%
      \setbox\figbox\hbox{\includegraphics[#3]{#4}}%
      \xdef\xfigwd{\the\wd\figbox}%
      \ifdim\wd\figbox<\columnwidth%
        \begin{figure}[#1]%
          \centering%
          \vspace*{5pt}%
          \vspace*{\fig@topskip}%
          \includegraphics[#3]{#4}%
          \vspace*{\fig@midskip}%
          \caption{#5}%
          \vspace*{\fig@botskip}%
        \end{figure}
      \else%
        \begin{figure*}[#1]%
          \centering%
          \vspace*{5pt}%
          \vspace*{\fig@topskip}%
          \includegraphics[#3]{#4}%
          \vspace*{\fig@midskip}%
          \caption{#5}%
          \vspace*{\fig@botskip}%
        \end{figure*}
      \fi%
}
%%%%%%%%%%%%

\define@key{tabkeys}{topskip}{\def\tab@topskip{#1}}
\define@key{tabkeys}{botskip}{\def\tab@botskip{#1}}
\define@key{tabkeys}{width}{\def\tab@width{#1}}
\define@key{tabkeys}{resize}{\def\tab@resize{#1}}
\define@key{tabkeys}{arraystretch}{\def\tab@arraystretch{#1}}
\setkeys{tabkeys}{topskip=0pt,botskip=0pt,width=\columnwidth,resize=!,arraystretch=1.3}%

\def\tab@excl{!}
\def\Table{\@ifnextchar[{\@Table}{\@Table[t!]}}
\def\@Table[#1]{\@ifnextchar({\@@Table[#1]}{\@@Table[#1](topskip=0pt)}}
\def\@@Table[#1](#2)#3#4{%
      \setkeys{tabkeys}{#2}%
      \ifdim\tab@width<\columnwidth%
        \begin{table}[#1]%
        \centering%
        \renewcommand\arraystretch{\tab@arraystretch}%
        \centerline{\parbox{\tab@width}{\caption{#3}}}%
        \ifx\tab@resize\tab@excl%
          {\tablebodyfont#4}%
        \else%
          \resizebox{\tab@resize}{!}{\tablebodyfont#4}%
        \fi%
        \end{table}%
      \else%
        \begin{table*}[#1]%
        \centering%
        \renewcommand\arraystretch{\tab@arraystretch}%
        \centerline{\parbox{\tab@width}{\caption{#3}}}%
        \ifx\tab@resize\tab@excl%
          {\tablebodyfont#4}%
        \else%
          \resizebox{\tab@resize}{!}{\tablebodyfont#4}%
        \fi%
        \end{table*}%
      \fi%
}

%%%
%headers
\def\headName{}
\def\@pubid{}
\def\markboth#1#2{\def\leftmark{#1}\def\rightmark{#2}}
\def\thevol{4}
\def\theyear{2016}
\def\vol#1{\gdef\thevol{#1}}
\def\year#1{\gdef\theyear{#1}}
\def\pubid#1{\gdef\@pubid{#1}}
\def\headname#1{\gdef\headName{#1}}
\ifjtehm
  \def\headerlogo{\raisebox{-2pt}{\includegraphics[width=7.61pc]{jtehmLogo.png}}}
  \def\ps@titlepage{%
     \def\@oddhead{\parbox[t]{\textwidth}{\mbox{}\\[-6.3mm]{\raisebox{5pt}%
       {{\titlepageheaderfont\color{accessblue}\headName}}}%
       \hfill\headerlogo\mbox{}\vspace*{-3.5mm}\par\rule{30.54pc}{.3pt}}}
     \def\@evenhead{\parbox[t]{\textwidth}{\mbox{}\\[-6.3mm]\mbox{}\headerlogo%
       \hfill{\raisebox{5pt}{{\titlepageheaderfont\color{accessblue}\headName}}}%
       \vspace*{-3.5mm}\par\mbox{}\hfill\rule{30.54pc}{.3pt}}}
     \def\@oddfoot{\raisebox{3pt}{%%
       \hbox to 0pc{\hbox to \textwidth{{\footervolfont VOLUME\ \thevol, \theyear}\hfill\mbox{}}}%
       \hbox to 0pc{\hbox to \textwidth{\mbox{}\hfill{\footervolfont\@pubid}\hfill\mbox{}}}%
       \hbox to 0pc{\hbox to \textwidth{\mbox{}\hfill{\footerpagefont\@artnum}}}%
       }}
     \def\@evenfoot{\raisebox{3pt}{%
       \hbox to 0pc{\hbox to \textwidth{{\footerpagefont\@artnum}}\hfill\mbox{}}\hspace*{1.8pc}%
       \hbox to 0pc{\hbox to \textwidth{\mbox{}\hfill{\footervolfont\@pubid}\hfill\mbox{}}}%
       \hbox to 0pc{\hbox to \textwidth{\mbox{}\hfill{\footervolfont VOLUME\ \thevol, \theyear}}}%
     }}
  }
  \def\ps@headings{%
     \def\@oddhead{\parbox[t]{\textwidth}{\mbox{}\\[-6.3mm]{\raisebox{5pt}%
       {\headerfont\rightmark}}\hfill\headerlogo\mbox{}\vspace*{-3.55mm}\par%
       \rule{30.54pc}{.3pt}}}
     \def\@evenhead{\parbox[t]{\textwidth}{\mbox{}\\[-6.3mm]\mbox{}%
       \headerlogo\hfill{\raisebox{5pt}{\headerfont\leftmark}}\vspace*{-3.55mm}\par%
       \mbox{}\hfill\rule{30.54pc}{.3pt}}}
     \def\@oddfoot{\raisebox{8pt}{%
       \hbox to 0pc{\hbox to \textwidth{{\footervolfont VOLUME\ \thevol, \theyear}\hfill\mbox{}}}%
       \hbox to 0pc{\hbox to \textwidth{\mbox{}\hfill{\footerpagefont\@artnum}}}%
       }}
     \def\@evenfoot{\raisebox{8pt}{%
       \hbox to 0pc{\hbox to \textwidth{{\footerpagefont\@artnum}\mbox{}\hfill}}%
       \hbox to 0pc{\hbox to \textwidth{\mbox{}\hfill{\footervolfont VOLUME\ \thevol, \theyear}}}%
     }}
  }
\else
  \def\headerlogo{\raisebox{-2pt}{\includegraphics[width=7.61pc]{Logo.png}}}
  \def\headerlogoall{\raisebox{-2pt}{\includegraphics[width=7.61pc]{notaglineLogo.png}}}
  \def\ps@titlepage{%
    \def\@oddhead{\parbox[t]{\textwidth}{\mbox{}\\[-6.3mm]\mbox{}\nheaderfont\color{accessblue}\headName\hfill\headerlogo{\raisebox{-2pt}{\,}}\color{black}\vspace*{-1.5mm}\par\hrulefill}}
    \def\@evenhead{\parbox[t]{\textwidth}{\mbox{}\\[-6.3mm]\mbox{}\headerlogo\hfill\nheaderfont\color{accessblue}\headName{\raisebox{-2pt}{\,}}\color{black}\vspace*{-1.5mm}\par\hrulefill}}
     \def\@oddfoot{\raisebox{3pt}{%%
%       \hbox to 0pc{\hbox to \textwidth{{\footervolfont VOLUME\ \thevol, 2016}\hfill\mbox{}}}%  REMOVED
       \hbox to 0pc{\hbox to \textwidth{\mbox{}\hfill{\footervolfont\@pubid}\hfill\mbox{}}}%
       \hbox to 0pc{\hbox to \textwidth{\mbox{}\hfill{\footerpagefont\thepage}}}%
       }}
     \def\@evenfoot{\raisebox{3pt}{%
       \hbox to 0pc{\hbox to \textwidth{{\footerpagefont\thepage}\hfill}\mbox{}}\hspace*{1.8pc}%
       \hspace*{-1.8pc}\hbox to 0pc{\hbox to \textwidth{\mbox{}\hfill{\footervolfont\@pubid}\hfill\mbox{}}}%
%       \hbox to 0pc{\hbox to \textwidth{\mbox{}\hfill{\footervolfont VOLUME\ \thevol, 2016}}}\hspace*{1.8pc}% REMOVED
     }}
  }
% normal page
  \def\ps@headings{%
     \def\@oddhead{\parbox[t]{\textwidth}{\mbox{}\\[-6.3mm]{\raisebox{-2pt}{\headerfont\rightmark}}\hfill\mbox{}\vspace*{-1.5mm}\par\hrulefill}}
     \def\@evenhead{\parbox[t]{\textwidth}{\mbox{}\\[-6.3mm]\mbox{}\hfill{\raisebox{-2pt}{\headerfont\leftmark}}\vspace*{-1.5mm}\par\hrulefill}}
     \def\@oddfoot{\raisebox{8pt}{%
%       \hbox to 0pc{\hbox to \textwidth{{\footervolfont VOLUME\ \thevol, 2016}\hfill\mbox{}}}%  REMOVED
       \hbox to 0pc{\hbox to \textwidth{\mbox{}\hfill{\footerpagefont\thepage}}}%
       }}
     \def\@evenfoot{\raisebox{8pt}{%
       \hbox to 0pc{\hbox to \textwidth{{\footerpagefont\thepage}\mbox{}\hfill}}\hspace*{1.8pc}%
%       \hspace*{-1.8pc}\hbox to 0pc{\hbox to \textwidth{\mbox{}\hfill{\footervolfont VOLUME\ \thevol, 2016}}}\hspace*{1.8pc}% REMOVED
     }}
  }
\fi
%%%
%title
\newlength\titlewidth
\newlength\abstractwidth
\ifjtehm
  \setlength\titlewidth{35.90pc}
  \let\abstractwidth\titlewidth
\else
  \setlength\titlewidth{152.83mm}
  \let\abstractwidth\titlewidth
  \advance\abstractwidth by -2.39mm
\fi
\newcounter{addrCtr}
\newsavebox\abstractbox
\newsavebox\indexbox

\def\abstracttitle{{\color{accessblue}\abstractheadfont ABSTRACT}\ifjtehm\quad\else\space\fi}
\def\indextitle{{\color{accessblue}\indexheadfont INDEX TERMS}\ifjtehm\quad\else\space\fi}
\def\history#1{\gdef\@history{#1}}\let\@history\@empty%
\def\artnum#1{\gdef\@artnum{#1}}
\def\doi#1{\gdef\@doi{#1}}
\def\title#1{\gdef\@title{#1}}
\def\corresp#1{\gdef\@corresp{#1}}\let\@corresp\@empty%
\def\tfootnote#1{\gdef\@tfootnote{#1}}\let\@tfootnote\@empty%
\def\author#1{\gdef\@author{#1}}
\def\address{\@ifnextchar[{\@address}{\@address[\unskip]}}
\def\@address[#1]#2{\stepcounter{addrCtr}%
     \expandafter\gdef\csname addrInd\theaddrCtr\endcsname{#1}%
     \expandafter\gdef\csname addr\theaddrCtr\endcsname{#2}%
}

\newdimen\absht
\renewenvironment{abstract}
     {\global\setbox99=\hbox\bgroup\noindent%
      \ifjtehm\else\raisebox{-.8pc}{\includegraphics[width=0.5em]{bullet.png}}\hspace*{1.5mm}\fi%
      \begin{minipage}[t]{\abstractwidth}%
      \abstracttitle\bodyfont%
     }
     {\end{minipage}%
      \egroup%
      \global\setlength\absht{\the\dp99}%
     }

\newdimen\kwdht
\ifdefined\keywords\else\newenvironment{keywords}{}{}\fi
\ifdefined\IEEEkeywords\else\newenvironment{IEEEkeywords}{}{}\fi
\renewenvironment{keywords}
     {\global\setbox88=\hbox\bgroup\noindent%
      \ifjtehm\else\raisebox{-.8pc}{\includegraphics[width=0.5em]{bullet.png}}\hspace*{1.5mm}\fi%
      \begin{minipage}[t]{\abstractwidth}%
      \indextitle\bodyfont%
     }
     {\end{minipage}%
      \egroup%
      \global\setlength\kwdht{\the\dp88}%
     }
\renewenvironment{IEEEkeywords}
     {\global\setbox88=\hbox\bgroup\noindent%
      \ifjtehm\else\raisebox{-.8pc}{\includegraphics[width=0.5em]{bullet.png}}\hspace*{1.5mm}\fi%
      \begin{minipage}[t]{\abstractwidth}%
      \indextitle\bodyfont%
     }
     {\end{minipage}%
      \egroup%
      \global\setlength\kwdht{\the\dp88}%
     }

\newcount\@tempcntc
\begingroup
  \catcode`P=12
  \catcode`T=12
  \lowercase{
    \def\x{\def\rem@dec##1.##2PT{##1}}}
  \expandafter\endgroup\x
\def\strip@dec{\expandafter\rem@dec\the}

\newskip\titlepgskip
\setlength\titlepgskip{0pt}
\def\docstrip#1.#2\@nil{#1}
\begingroup
  \catcode`P=12
  \catcode`T=12
  \lowercase{
    \def\x{\def\rem@pt##1.##2PT{##1\ifnum##2>\z@.##2\fi}}}
  \expandafter\endgroup\x
\def\strip@pt{\expandafter\rem@pt\the}
\def\fixSkip#1{%
     \@tempdima=#1%
     \advance\@tempdima by 12pt%
     \multiply\@tempdima by 2%
     \xdef\actualht{\the\@tempdima}%
     \multiply\@tempdima by 10%
     \divide\@tempdima by 12%
     \xdef\efg{\strip@pt\@tempdima}%
     \xdef\jag{\expandafter\docstrip\efg\@nil}%
     \@tempcnta=\jag%
     \divide\@tempcnta by 10%
     \multiply\@tempcnta by 12%
     \xdef\projectedht{\the\@tempcnta pt}%
     \@tempdimb=\actualht%
     \advance\@tempdimb by -\projectedht%
     \xdef\roundinght{\the\@tempdimb}%
     \box\maketitlebox%
     \vspace*{\roundinght}%
     \vspace*{3.5pt}%
     \vspace*{\titlepgskip}%
}

\newsavebox\maketitlebox
\def\@jtehmmaketitle{%
     \setbox\maketitlebox\hbox\bgroup%
     \begin{tabular*}{\textwidth}{@{}p{2.96pc}@{}p{\titlewidth}@{}p{3.15pc}@{}}%
     &\begin{center}\vspace*{1.2mm}\vspace*{-1.21pc}\centering%
     {\vss\historyfont\@history\vss}\vspace*{2mm}\par%
     {\vss\color{accessblue}\titlefont\@title\vss}\vspace*{6mm}\par%
     \ifjtehmeditorial\else{\vss\authorfont\@author\vss}\vspace*{1mm}\par%
       \@tempdima=\absht%
       \xdef\abc{\strip@dec\@tempdima}%
       \@tempcntb=\abc%
       \@tempcnta=0%
       \@tempcntc=0%
       \raisebox{-6pt}{\llap{\smash{\parbox[t]{2pc}{%
       \loop\ifnum\@tempcnta<\@tempcntb%
       \advance\@tempcnta by 12%
       \advance\@tempcntc by 1%
       \strut%
       {\strut\mbox{}\abstractfont\vphantom{X}\strut}\strut\\%
        \repeat\vspace*{2pt}%
       }}}}%
     \noindent\box99\vspace{6mm}\par%
     \@tempcnta=0%
     \loop\ifnum\@tempcnta<\theaddrCtr%
       \advance\@tempcnta by 1%
       \par{\vss\addressfont\textsuperscript{\expandafter\csname addrInd\the\@tempcnta\endcsname}%
        \expandafter\csname addr\the\@tempcnta\endcsname\vss}%
     \repeat\vspace*{1mm}\par\fi%
     {\vss\correspfont\@corresp\vss\vspace{2mm}}\par%
     \ifjtehmeditorial\else{\vss\tfootnotefont\@tfootnote\vss\vspace{7mm}}\fi\end{center}\par%
     \ifjtehmeditorial\else\vspace*{-.4pc}\hrulefill\par\fi%
       {\strut\mbox{}\abstractfont\vphantom{X}\strut}\strut\\%
     \noindent\box88\par\vspace*{.7pc}\hrulefill\par\vspace{20mm}\par\fi%
     &\end{tabular*}\par%
     \egroup%
     \fixSkip{\the\ht\maketitlebox}%
}
\def\@maketitle{%
     \setbox\maketitlebox\hbox\bgroup%
     \begin{minipage}{\titlewidth}%
     \raggedright\vspace*{1.2mm}%
%     \ifaccesseditors\else{\vss\historyfont\@history\vss}\vspace*{2mm}\par\fi%  REMOVED - hides Digital Object Identifier line
     {\vss\color{accessblue}\titlefont\@title\vss}\vspace*{6mm}\par%
     \ifaccesseditors\vspace*{2mm}\else{\vss\authorfont\@author\vss}\vspace*{0mm}\par%
     \@tempcnta=0%
     \loop\ifnum\@tempcnta<\theaddrCtr%
       \advance\@tempcnta by 1%
       \par{\vss\addressfont\textsuperscript{\expandafter\csname addrInd\the\@tempcnta\endcsname}%
        \expandafter\csname addr\the\@tempcnta\endcsname\vss}%
     \repeat\vspace*{1mm}\par%
     {\vss\correspfont\@corresp\vss\vspace{2mm}}\par\fi%
     {\vss\tfootnotefont\@tfootnote\vss\vspace{7mm}}\par%
     \noindent\box99\vspace{6mm}\par%
     \ifaccesseditors\vspace*{8mm}\else%
     \noindent\box88\vspace{18mm}\par%
     \fi%
     \end{minipage}\par%
     \egroup%
     \fixSkip{\the\ht\maketitlebox}%
}
\def\editorialmaketitle{\thispagestyle{titlepage}\onecolumngrid%
     \noindent\begin{minipage}[b]{\titlewidth}%
     \raggedright%
     {\vss\color{accessblue}\titlefont\@title\vss}\vspace*{6mm}\par%
     \end{minipage}\par%
}
\def\maketitle{\ifaccesseditorial%
     \ifjtehmeditorial\twocolumn[{\thispagestyle{titlepage}\@jtehmmaketitle%
     \vskip 0.3\baselineskip plus 0.1\baselineskip minus 0.1\baselineskip%
     \vspace*{\baselineskip}}]\fi%
     \else\twocolumn[\thispagestyle{titlepage}\ifjtehm\@jtehmmaketitle\else\@maketitle\fi%
     \vskip 0.3\baselineskip plus 0.1\baselineskip minus 0.1\baselineskip%
     \ifjtehm\vspace*{\baselineskip}\else\vspace*{-1pt}\vspace*{-24pt}\fi]\fi}%
\ps@headings
\pagenumbering{arabic}
\flushbottom
\emergencystretch=2pt


\def\IEEEmembership#1{{\membershipfont(#1)}}

\ifjtehm
  \def\burl#1{%
    \@tfor\xx:=#1\do{%
    \href{#1}{\xx}\linebreak[0]%
    }%
  }%
  \RequirePackage[hidelinks=true,bookmarks=false]{hyperref}%
\fi

%%%
%bibliography
\def\@biblabel#1{[#1]}
\def\refname{REFERENCES}
\def\thebibliography#1{%
    \restoreSection%
    \section*{\refname}%
    \addcontentsline{toc}{section}{\refname}%
    \normalfont\referencefont\vskip 0.3\baselineskip plus 0.1\baselineskip minus 0.1\baselineskip%
    \list{\@biblabel{\@arabic\c@enumiv}}%
    {\settowidth\labelwidth{\@biblabel{#1}}%
    \leftmargin\labelwidth
    \advance\leftmargin\labelsep\relax
    \itemsep 0pt plus .5pt\relax%
    \usecounter{enumiv}%
    \let\p@enumiv\@empty
    \renewcommand\theenumiv{\@arabic\c@enumiv}}%
    \let\@IEEElatexbibitem\bibitem%
    \def\bibitem{\@IEEEbibitemprefix\@IEEElatexbibitem}%
\def\newblock{\hskip .11em plus .33em minus .07em}%
\sloppy\clubpenalty4000\widowpenalty4000\interlinepenalty500%
    \sfcode`\.=1000\relax}
\let\endthebibliography=\endlist
%%%
%biography
\ifdefined\biography\else\newenvironment{biography}{}{}\fi
\ifdefined\IEEEbiography\else\newenvironment{IEEEbiography}{}{}\fi
\ifdefined\biographynophoto\else\newenvironment{biographynophoto}{}{}\fi
\ifdefined\IEEEbiographynophoto\else\newenvironment{IEEEbiographynophoto}{}{}\fi
\renewenvironment{biography}[2][]{\normalfont\biographyfont%
\unitlength 1in\parskip=0pt\par\parindent 1em\interlinepenalty500%
\@IEEEtrantmpdimenA=\@IEEEBIOhangdepth%
\advance\@IEEEtrantmpdimenA by \@IEEEBIOskipN%
\advance\@IEEEtrantmpdimenA by 1\baselineskip%
\@IEEEtranneedspace{\@IEEEtrantmpdimenA}{\relax}%
\vskip \@IEEEBIOskipN plus 1fil minus 0\baselineskip%
\def\@IEEEtempbiographybox{{\setlength{\fboxsep}{0pt}\framebox{\begin{minipage}[b][\@IEEEBIOphotodepth][c]{\@IEEEBIOphotowidth}\centering PLACE\\ PHOTO\\ HERE \end{minipage}}}}%
\@ifmtarg{#1}{\relax}{\def\@IEEEtempbiographybox{\mbox{\begin{minipage}[b][\@IEEEBIOphotodepth][c]{\@IEEEBIOphotowidth}%
\centering%
#1%
\end{minipage}}}}%
\addcontentsline{toc}{subsection}{#2}%
\let\@IEEEBIOORGparCMD=\par%
\edef\par{\hfil\break\indent}%
\settoheight{\@IEEEtrantmpdimenA}{\@IEEEtempbiographybox}%
\@IEEEtrantmpdimenB=\@IEEEBIOhangdepth%
\@IEEEtrantmpcountA=\@IEEEtrantmpdimenB%
\divide\@IEEEtrantmpcountA by \baselineskip%
\advance\@IEEEtrantmpcountA by 1%
\hangindent\@IEEEBIOhangwidth%
\hangafter-\@IEEEtrantmpcountA%
\settoheight{\@IEEEtrantmpdimenB}{\mbox{T}}%
\noindent\makebox[0pt][l]{\hspace{-\@IEEEBIOhangwidth}\raisebox{\@IEEEtrantmpdimenB}[0pt][0pt]{\raisebox{-\@IEEEBIOphotodepth}[0pt][0pt]{\@IEEEtempbiographybox}}}%
\noindent{\biographyheadfont\uppercase {#2}\ }\@IEEEgobbleleadPARNLSP}{\relax\let\par=\@IEEEBIOORGparCMD\par%
\ifnum \prevgraf <\@IEEEtrantmpcountA\relax%
    \advance\@IEEEtrantmpcountA by -\prevgraf%
    \advance\@IEEEtrantmpcountA by -1\relax%
    \@IEEEtrantmpdimenA=\baselineskip%
    \multiply\@IEEEtrantmpdimenA by \@IEEEtrantmpcountA%
    \noindent\rule{0pt}{\@IEEEtrantmpdimenA}%
\fi%
\par\normalfont}
\renewenvironment{IEEEbiography}[2][]{\normalfont\biographyfont%
\unitlength 1in\parskip=0pt\par\parindent 1em\interlinepenalty500%
\@IEEEtrantmpdimenA=\@IEEEBIOhangdepth%
\advance\@IEEEtrantmpdimenA by \@IEEEBIOskipN%
\advance\@IEEEtrantmpdimenA by 1\baselineskip%
\@IEEEtranneedspace{\@IEEEtrantmpdimenA}{\relax}%
\vskip \@IEEEBIOskipN plus 1fil minus 0\baselineskip%
\def\@IEEEtempbiographybox{{\setlength{\fboxsep}{0pt}\framebox{\begin{minipage}[b][\@IEEEBIOphotodepth][c]{\@IEEEBIOphotowidth}\centering PLACE\\ PHOTO\\ HERE \end{minipage}}}}%
\@ifmtarg{#1}{\relax}{\def\@IEEEtempbiographybox{\mbox{\begin{minipage}[b][\@IEEEBIOphotodepth][c]{\@IEEEBIOphotowidth}%
\centering%
#1%
\end{minipage}}}}%
\addcontentsline{toc}{subsection}{#2}%
\let\@IEEEBIOORGparCMD=\par%
\edef\par{\hfil\break\indent}%
\settoheight{\@IEEEtrantmpdimenA}{\@IEEEtempbiographybox}%
\@IEEEtrantmpdimenB=\@IEEEBIOhangdepth%
\@IEEEtrantmpcountA=\@IEEEtrantmpdimenB%
\divide\@IEEEtrantmpcountA by \baselineskip%
\advance\@IEEEtrantmpcountA by 1%
\hangindent\@IEEEBIOhangwidth%
\hangafter-\@IEEEtrantmpcountA%
\settoheight{\@IEEEtrantmpdimenB}{\mbox{T}}%
\noindent\makebox[0pt][l]{\hspace{-\@IEEEBIOhangwidth}\raisebox{\@IEEEtrantmpdimenB}[0pt][0pt]{\raisebox{-\@IEEEBIOphotodepth}[0pt][0pt]{\@IEEEtempbiographybox}}}%
\noindent{\biographyheadfont\uppercase {#2}\ }\@IEEEgobbleleadPARNLSP}{\relax\let\par=\@IEEEBIOORGparCMD\par%
\ifnum \prevgraf <\@IEEEtrantmpcountA\relax%
    \advance\@IEEEtrantmpcountA by -\prevgraf%
    \advance\@IEEEtrantmpcountA by -1\relax%
    \@IEEEtrantmpdimenA=\baselineskip%
    \multiply\@IEEEtrantmpdimenA by \@IEEEtrantmpcountA%
    \noindent\rule{0pt}{\@IEEEtrantmpdimenA}%
\fi%
\par\normalfont}

\renewenvironment{biographynophoto}[1]{%
\if@biographyTOCentrynotmade%
\setcounter{biography}{-1}%
\refstepcounter{biography}%
\addcontentsline{toc}{section}{Biographies}%
\global\@biographyTOCentrynotmadefalse%
\fi%
\refstepcounter{biography}%
\addcontentsline{toc}{subsection}{#1}%
\normalfont\biographyfont\interlinepenalty500%
\vskip 4\baselineskip plus 1fil minus 0\baselineskip%
\parskip=0pt\par%
\noindent{\biographyheadfont\uppercase{#1}\ }\@IEEEgobbleleadPARNLSP}{\relax\par\normalfont}
\renewenvironment{IEEEbiographynophoto}[1]{%
\if@biographyTOCentrynotmade%
\setcounter{biography}{-1}%
\refstepcounter{biography}%
\addcontentsline{toc}{section}{Biographies}%
\global\@biographyTOCentrynotmadefalse%
\fi%
\refstepcounter{biography}%
\addcontentsline{toc}{subsection}{#1}%
\normalfont\biographyfont\interlinepenalty500%
\vskip 4\baselineskip plus 1fil minus 0\baselineskip%
\parskip=0pt\par%
\noindent{\biographyheadfont\uppercase{#1}\ }\@IEEEgobbleleadPARNLSP}{\relax\par\normalfont}

\def\EOD{\ifaccesseditors\else\mbox{}\newline\hspace*{\fill}\mbox{\rotatebox{90}{\includegraphics[width=0.5em]{bullet.png}}}\fi\global\eoddefinedtrue}

\ifaccesseditors
\def\bioaddressfont{\sffamily\putfont{T1}{formata}{n}{n}{8}{10}}
\def\bionamefont{\sffamily\fontencoding{T1}\fontseries{m}\fontsize{10}{12}\selectfont}%
\let\biobodyfont\biographyfont

\newenvironment{ebbiography}[3][]{\normalfont\biobodyfont%
\unitlength 1in\parskip=0pt\par\parindent 1em\interlinepenalty500%
\@IEEEtrantmpdimenA=\@IEEEBIOhangdepth%
\advance\@IEEEtrantmpdimenA by \@IEEEBIOskipN%
\advance\@IEEEtrantmpdimenA by 1\baselineskip%
\@IEEEtranneedspace{\@IEEEtrantmpdimenA}{\relax}%
\def\@IEEEtempbiographybox{{\setlength{\fboxsep}{0pt}\framebox{\begin{minipage}[b][\@IEEEBIOphotodepth][c]{\@IEEEBIOphotowidth}\centering PLACE\\ PHOTO\\ HERE \end{minipage}}}}%
\@ifmtarg{#1}{\relax}{\def\@IEEEtempbiographybox{\mbox{\begin{minipage}[b][\@IEEEBIOphotodepth][c]{\@IEEEBIOphotowidth}%
\centering%
#1%
\end{minipage}}}}%
\addcontentsline{toc}{subsection}{#2}%
\let\@IEEEBIOORGparCMD=\par%
\edef\par{\hfil\break\indent}%
\settoheight{\@IEEEtrantmpdimenA}{\@IEEEtempbiographybox}%
\@IEEEtrantmpdimenB=\@IEEEBIOhangdepth%
\@IEEEtrantmpcountA=\@IEEEtrantmpdimenB%
\divide\@IEEEtrantmpcountA by \baselineskip%
\advance\@IEEEtrantmpcountA by 1%
\hangindent\@IEEEBIOhangwidth%
\hangafter-\@IEEEtrantmpcountA%
\settoheight{\@IEEEtrantmpdimenB}{\mbox{T}}%
\noindent\makebox[0pt][l]{\hspace{-\@IEEEBIOhangwidth}\raisebox{\@IEEEtrantmpdimenB}[0pt][0pt]{\raisebox{-\@IEEEBIOphotodepth}[0pt][0pt]{\@IEEEtempbiographybox}}}%
\noindent{\rightskip 0pt plus 1fil\bionamefont#2\\\bioaddressfont#3}\@IEEEgobbleleadPARNLSP}{\relax\let\par=\@IEEEBIOORGparCMD\par%
\ifnum \prevgraf <\@IEEEtrantmpcountA\relax%
    \advance\@IEEEtrantmpcountA by -\prevgraf%
    \advance\@IEEEtrantmpcountA by -1\relax%
    \@IEEEtrantmpdimenA=\baselineskip%
    \multiply\@IEEEtrantmpdimenA by \@IEEEtrantmpcountA%
    \noindent\rule{0pt}{\@IEEEtrantmpdimenA}%
\fi%
\par\biobodyfont}

\newenvironment{ebbiographynophoto}[1]{%
\addcontentsline{toc}{subsection}{#1}%
\normalfont\biobodyfont\interlinepenalty500%
\vspace{\baselineskip}%
\parskip=0pt\par%
\noindent{{\biographyheadfont #1}\ }\@IEEEgobbleleadPARNLSP}{\relax\par\biobodyfont}

\newenvironment{editorialbiography}[4][]{%
\begin{ebbiography}[{\includegraphics[width=1in,height=1.25in,clip,keepaspectratio]{#1}}]{#2}{#3}
\end{ebbiography}\par\begin{ebbiographynophoto}{#4}}
    {\end{ebbiographynophoto}\vspace{2\baselineskip}}
\fi

\AtEndDocument{%
  \ifjtehm\else%
   \ifeoddefined\else%
   \ClassError{ieeeaccess}
     {You have not used the command \string\EOD\space at the end of \MessageBreak
      last para in the document. I have reached end of the document searching for it}%
     {Please put the macro \string\EOD\space in the end of the last para. 
     (End of last biography or end of last reference.)}%
   \fi%
  \fi%
}

\AtBeginDocument{%
\gdef\operator@encoding{T1}
\gdef\encodingdefault{T1}
\def\bf{\fontencoding{T1}\fontseries{b}\selectfont}
\def\rm{\fontencoding{T1}\selectfont}
}

\def\headeretal{{\iheaderfont et al.}}

\ifdefined\PARstart\ifdefined\IEEEPARstart\else\let\IEEEPARstart\PARstart\fi\fi
\ifdefined\IEEEPARstart\ifdefined\PARstart\else\let\PARstart\IEEEPARstart\fi\fi

\endinput