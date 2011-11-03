# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/subeqnarray
# catalog-date 2007-01-02 10:01:06 +0100
# catalog-license lppl
# catalog-version 2.1c
Name:		texlive-subeqnarray
Version:	2.1c
Release:	1
Summary:	Equation array with sub numbering
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/subeqnarray
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subeqnarray.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subeqnarray.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subeqnarray.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package defines the subeqnarray and subeqnarray*
environments, which behave like the equivalent eqnarray and
eqnarray* environments, except that the individual lines are
numbered like 1a, 1b, 1c, etc. To refer to these numbers an
extra label command \slabel is provided.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}