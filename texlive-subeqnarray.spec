%global tl_name subeqnarray
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1f
Release:	%{tl_revision}.1
Summary:	Equation array with sub numbering
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/subeqnarray
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subeqnarray.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subeqnarray.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subeqnarray.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package defines the subeqnarray and subeqnarray* environments,
which behave like the corresponding eqnarray and eqnarray* environments,
except that the individual lines are numbered like 1a, 1b, 1c, etc. To
refer to these numbers an extra label command \slabel is provided. Users
are urged to consider the alignment capabilities of the amsmath bundle,
which produce better results than eqnarray-related macros.

