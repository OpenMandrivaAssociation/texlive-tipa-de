# revision 22005
# category Package
# catalog-ctan /info/translations/tipa/de
# catalog-date 2011-04-06 08:36:04 +0200
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-tipa-de
Version:	1.3
Release:	1
Summary:	German translation of tipa documentation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/tipa/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tipa-de.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tipa-de.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
