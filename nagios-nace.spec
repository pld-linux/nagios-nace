%include	/usr/lib/rpm/macros.perl
Summary:	Nagios Automated Configuration Engine
Summary(pl.UTF-8):	Nagios Automated Configuration Engine - silnik do automatycznej konfituracji Nagiosa
Name:		nagios-nace
Version:	0.4
Release:	0.1
Epoch:		0
License:	GPL v2
Group:		Applications
Source0:	http://www.adamsinfoserv.com/software/nace-%{version}.tar.gz
# Source0-md5:	4f77d43795946c2544fe2f6c0e620bad
URL:		http://www.adamsinfoserv.com/AISTWiki/bin/view/AIS/NACE
BuildRequires:	sed >= 4.0
BuildArch:	noarch
Obsoletes:	nace
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir %{_datadir}/nace

%description
NACE is a generic query engine used to automatically create host and
service definitions for hosts on the network.

It is intended to be used in a shell script at regular intervals by an
experienced Nagios administrator to perform a query against the
supplied host list. It then creates host and service definitions using
the parameters supplied in the query.

%description -l pl.UTF-8
NACE to ogólny silnik odpytujący służący do automatycznego tworzenia
definicji hostów i usług dla hostów w sieci.

Jest przeznaczony do używania jako skrypt powoki w regularnych
odstępach czasu przez doświadczonego administratora Nagiosa do
sprawdzania podanej listy hostów. Następnie tworzy definicje hostów i
usług przy użyciu parametrów przekazanych do zapytania.

%prep
%setup -q -n nace-%{version}

#sed -i -e '
#s#DebugMsg \(.*\);#DebugMsg(\1);#g
#' scripts/*.pl 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}/{bin,lib}

cp -a bin/* $RPM_BUILD_ROOT%{_appdir}/bin
cp -a lib/* $RPM_BUILD_ROOT%{_appdir}/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL README README.old REQUIREMENTS THANKS TODO SCRIPTS
%dir %{_appdir}
%dir %{_appdir}/bin
%attr(755,root,root) %{_appdir}/bin/*
%{_appdir}/lib
