Name:		texlive-subeqnarray
Version:	15878
Release:	1
Summary:	Equation array with sub numbering
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/subeqnarray
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subeqnarray.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subeqnarray.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subeqnarray.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package defines the subeqnarray and subeqnarray*
environments, which behave like the equivalent eqnarray and
eqnarray* environments, except that the individual lines are
numbered like 1a, 1b, 1c, etc. To refer to these numbers an
extra label command \slabel is provided.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/subeqnarray/subeqnarray.sty
%doc %{_texmfdistdir}/doc/latex/subeqnarray/manifest.txt
%doc %{_texmfdistdir}/doc/latex/subeqnarray/subeqnarray.pdf
%doc %{_texmfdistdir}/doc/latex/subeqnarray/subeqnarray.tex
#- source
%doc %{_texmfdistdir}/source/latex/subeqnarray/subeqnarray.dtx
%doc %{_texmfdistdir}/source/latex/subeqnarray/subeqnarray.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
