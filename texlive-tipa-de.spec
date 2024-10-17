Name:		texlive-tipa-de
Version:	22005
Release:	2
Summary:	German translation of tipa documentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/translations/tipa/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tipa-de.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tipa-de.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is a translation of Fukui Rei's tipaman from the tipa
bundle.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/tipa-de/LIESMICH
%doc %{_texmfdistdir}/doc/latex/tipa-de/tipa.bib
%doc %{_texmfdistdir}/doc/latex/tipa-de/tipaman-de.pdf
%doc %{_texmfdistdir}/doc/latex/tipa-de/tipaman-de.tex
%doc %{_texmfdistdir}/doc/latex/tipa-de/tipaman0-de.tex
%doc %{_texmfdistdir}/doc/latex/tipa-de/tipaman1-de.tex
%doc %{_texmfdistdir}/doc/latex/tipa-de/tipaman2-de.tex
%doc %{_texmfdistdir}/doc/latex/tipa-de/tipaman3-de.tex
%doc %{_texmfdistdir}/doc/latex/tipa-de/tipaman4-de.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
