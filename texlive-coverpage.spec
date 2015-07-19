# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/coverpage
# catalog-date 2007-03-05 15:26:58 +0100
# catalog-license lppl
# catalog-version 1.01
Name:		texlive-coverpage
Version:	1.01
Release:	11
Summary:	Automatic cover page creation for scientific papers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/coverpage
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coverpage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coverpage.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coverpage.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.01-2
+ Revision: 750579
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.01-1
+ Revision: 718160
- texlive-coverpage
- texlive-coverpage
- texlive-coverpage
- texlive-coverpage

