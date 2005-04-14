Summary:	command line tool for non-destructive resizing of FAT16/FAT32 file systems
Name:		fatresize
Version:	1.0.1
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/fatresize/%{name}-%{version}.tar.bz2
# Source0-md5:	f4b03531e9bdba979932248f6a89bdfd
URL:		http://sourceforge.net/projects/fatresize/
BuildRequires:	parted-devel >= 1.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fatresize is a command line tool for non-destructive resizing of
FAT16/FAT32 file systems. It is based on the GNU Parted library. The
main target of the project is to be used with the EVMS FAT plugin.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING CREDITS ChangeLog NEWS README

#%%dir %{_sysconfdir}
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*

%attr(755,root,root) %{_sbindir}/*

#%attr(754,root,root) /etc/rc.d/init.d/%{name}
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
