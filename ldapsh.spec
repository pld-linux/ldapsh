%include	/usr/lib/rpm/macros.perl
Summary:	LDAP shell entirely written in Perl
Name:		ldapsh
Version:	0.9.4pre1
Release:	0.2
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/ldapsh/%{name}-%{version}.tar.gz
# Source0-md5:	35f073a7a1fce88ef930cc2a1ea7c09a
URL:		http://ldapsh.sourceforge.net/
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl(Net::LDAP)
Requires:	perl(Devel::Symdump)
Requires:	perl(Pod::Select)
Requires:	perl(File::Temp)
Requires:	perl(IO::Socket::SSL)
Requires:	perl(Pod::Text::Termcap)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an LDAP shell entirely written in Perl.With it, you can search
entries, apply some changes to them (massive updates), display some
entry attributes... The shell support command completion,
DN completion, online help and a lot of more features.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/skel}

install ldapsh $RPM_BUILD_ROOT%{_bindir}
install ldapshrc $RPM_BUILD_ROOT%{_sysconfdir}/skel/.ldapshrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README ldapsh.html ldapsh.css
%attr(755,root,root) %{_bindir}/%{name}
%{_sysconfdir}/skel/.ldapshrc
