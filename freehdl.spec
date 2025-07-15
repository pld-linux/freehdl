#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	freehdl
Name:		freehdl
Version:	0.0.6
Release:	0.1
License:	GPL
# library is under lgpl but its not separated as package so all falls under GPL imo
Group:		Applications
Source0:	http://%{name}.seul.org/~enaroska/freehdl-%{version}.tar.gz
# Source0-md5:	bd168382c72f9fbd392f89ab2c5fddf8
URL:		http://freehdl.seul.org/
#BuildRequires:	-
#BuildRequires:	autoconf
#BuildRequires:	automake
#BuildRequires:	intltool
#BuildRequires:	libtool
#Patch0: %{name}-DESTDIR.patch
#Requires(postun):	-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires:	-
#Provides:	-
#Provides:	group(foo)
#Provides:	user(foo)
#Obsoletes:	-
#Conflicts:	-
#BuildArch:	noarch
#ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreeHDL is an project aiming to develop VHDL simulator with following capabilities:
 * Has a graphical waveform viewer.
 * Has a source level debugger.
 * Is VHDL-93 compliant.
 * Is of commercial quality. (on par with, say, V-System - it'll take us a while to get there, but that should be our aim)

%prep
%setup -q
#%setup -q -c -T
#%setup -q -n %{name}
#%setup -q -n %{name}-%{version}.orig -a 1
#%%patch0 -p1

# undos the source
#find '(' -name '*.php' -o -name '*.inc' ')' -print0 | xargs -0 %{__sed} -i -e 's,\r$,,'

# remove CVS control files
#find -name CVS -print0 | xargs -0 rm -rf

# you'll need this if you cp -a complete dir in source
# cleanup backups after patching
#find . '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__intltoolize}
#%%{__gettextize}
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
# if not running libtool or automake, but config.sub is too old:
#cp -f /usr/share/automake/config.sub .
%configure
%{__make}

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/
#install AUTHORS COPYING COPYING.LIB README README.AIRE README.gen-nodes README.libraries README.v2cc README.vaul ChangeLog $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING.LIB README README.AIRE README.gen-nodes README.libraries README.v2cc README.vaul ChangeLog
%attr(755,root,root) %{_libdir}/*.so*
%{_libdir}/*.la
%{_libdir}/*.a
%dir %{_libdir}/freehdl
%attr(755,root,root) %{_libdir}/freehdl/*.so*
%{_libdir}/freehdl/*.la
%{_libdir}/freehdl/*.a
%{_datadir}/freehdl
%dir %{_includedir}/freehdl
%{_includedir}/freehdl/*h
%{_includedir}/freehdl/*t
%attr(755,root,root) %{_bindir}/*
%{_pkgconfigdir}/freehdl.pc
#%{_docdir}/%{name}-%{version}
%{_mandir}/man[15]/*
