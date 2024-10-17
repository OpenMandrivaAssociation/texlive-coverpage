Name:		texlive-coverpage
Version:	63509
Release:	2
Summary:	Automatic cover page creation for scientific papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/coverpage
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coverpage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coverpage.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coverpage.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package CoverPage was created to supplement scientific
papers with a cover page containing bibliographical
information, a copyright notice, and/or some logos of the
author's institution. The cover page is created (almost)
automatically; this is done by parsing BibTeX information
corresponding to the main document and reading a configuration
file in which the author can set information like the
affiliation he or she is associated with. The cover page
consists of header, body and footer; all three are macros which
can be redefined using \renewcommand, thus allowing easy
customization of the package. Additionally, it should be
stressed that the cover page layout is totally independent of
the main document and its page layout. This package requires
four other packages (keyval, url, textcomp, and verbatim), but
all of them are standard packages and should be part of every
LaTeX installation.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/coverpage/CoverPage.cfg
%{_texmfdistdir}/tex/latex/coverpage/CoverPage.sty
%doc %{_texmfdistdir}/doc/latex/coverpage/CoverPage.pdf
%doc %{_texmfdistdir}/doc/latex/coverpage/ECCV06Sample.pdf
%doc %{_texmfdistdir}/doc/latex/coverpage/README
%doc %{_texmfdistdir}/doc/latex/coverpage/SimpleSample.BibTeX.txt
%doc %{_texmfdistdir}/doc/latex/coverpage/SimpleSample.pdf
%doc %{_texmfdistdir}/doc/latex/coverpage/SimpleSample.tex
#- source
%doc %{_texmfdistdir}/source/latex/coverpage/CoverPage.dtx
%doc %{_texmfdistdir}/source/latex/coverpage/CoverPage.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
