Name:           glibmm24
Version:        2.22.1
Release:        1%{?dist}
Summary:        C++ interface for GTK2 (a GUI library for X)

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://gtkmm.sourceforge.net/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/glibmm/2.22/glibmm-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libsigc++20-devel >= 2.0.0
BuildRequires:  glib2-devel >= 2.21.1


%description
glibmm provides a C++ interface to the GTK+ GLib low-level core
library. Highlights include typesafe callbacks, widgets extensible via
inheritance and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.


%package devel
Summary:        Headers for developing programs that will use %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       glib2-devel
Requires:       libsigc++20-devel


%description devel
This package contains the static libraries and header files needed for
developing glibmm applications.


%package        doc
Summary:        Documentation for %{name}, includes full API docs
Group:          Documentation


%description    doc
This package contains the full API documentation for %{name}.


%prep
%setup -q -n glibmm-%{version}


%build
%configure %{!?_with_static: --disable-static}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -rf tools
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

# Fix documentation installation, put everything under gtk-doc
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/glibmm-2.4
mv ${RPM_BUILD_ROOT}%{_docdir}/glibmm-2.4/* $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/glibmm-2.4/
mv ${RPM_BUILD_ROOT}%{_datadir}/devhelp/books/glibmm-2.4/*.devhelp2 $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/glibmm-2.4/
# Fix devhelp broken base tag
sed -i 's:base="[^\"]*":base="/usr/share/gtk-doc/html/glibmm-2.4/reference/html":' ${RPM_BUILD_ROOT}%{_datadir}/gtk-doc/html/glibmm-2.4/*.devhelp2
# Remove old doc directory
rm -fr ${RPM_BUILD_ROOT}%{_datadir}/doc/glibmm-2.4


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, -)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*


%files devel
%defattr(-, root, root, -)
%{_includedir}/glibmm-2.4
%{_includedir}/giomm-2.4
%{?_with_static: %{_libdir}/*.a}
%{_libdir}/*.so
%{_libdir}/glibmm-2.4
%{_libdir}/giomm-2.4
%{_libdir}/pkgconfig/*.pc
%{_datadir}/glibmm-2.4
%{_datadir}/aclocal/*.m4


%files doc
%defattr(-, root, root, -)
%doc %{_datadir}/gtk-doc/html/glibmm-2.4


%changelog
* Fri Sep 25 2009 Denis Leroy <denis@poolshark.org> - 2.22.1-1
- Update to upstream 2.22.1

* Tue Sep 15 2009 Denis Leroy <denis@poolshark.org> - 2.21.5-2
- Better fix for devhelp file broken tags

* Mon Sep 14 2009 Denis Leroy <denis@poolshark.org> - 2.21.5-1
- Update to upstream 2.21.5
- Keep datadir/glibmm-2.4, for doc scripts

* Wed Sep  2 2009 Denis Leroy <denis@poolshark.org> - 2.21.4.2-1
- Update to upstream 2.21.4.2

* Sun Aug 30 2009 Denis Leroy <denis@poolshark.org> - 2.21.4-1
- Update to upstream 2.21.4

* Sun Aug 16 2009 Denis Leroy <denis@poolshark.org> - 2.21.3-1
- Update to upstream 2.21.3

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul  9 2009 Denis Leroy <denis@poolshark.org> - 2.21.1-1
- Update to upstream 2.21.1
- Switch to unstable branch, to follow glib2 version

* Sat Mar 21 2009 Denis Leroy <denis@poolshark.org> - 2.20.0-1
- Update to 2.20.0

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 14 2009 Denis Leroy <denis@poolshark.org> - 2.19.2-1
- Update to upstream 2.19.2
- Some new API, memory leak fix

* Wed Jan 14 2009 Denis Leroy <denis@poolshark.org> - 2.19.1-1
- Update to upstream 2.19.1

* Thu Dec 11 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.18.1-2
- Rebuild for pkgconfig provides

* Tue Oct 21 2008 Denis Leroy <denis@poolshark.org> - 2.18.1-1
- Update to upstream 2.18.1, many bug fixes
- Patch for define conflict upstreamed

* Sat Oct 11 2008 Denis Leroy <denis@poolshark.org> - 2.18.0-4
- Split documentation in new doc sub-package
- Fixed some devhelp documentation links

* Sun Oct 05 2008 Adel Gadllah <adel.gadllah@gmail.com> - 2.18.0-3
- Patch error.h directly rather than error.hg

* Sun Oct 05 2008 Adel Gadllah <adel.gadllah@gmail.com> - 2.18.0-2
- Backport upstream fix that resolves HOST_NOT_FOUND
  symbol conflicts (GNOME #529496)

* Tue Sep 23 2008 Denis Leroy <denis@poolshark.org> - 2.18.0-1
- Update to upstream 2.18.0

* Sun Aug 24 2008 Denis Leroy <denis@poolshark.org> - 2.17.2-1
- Update to upstream 2.17.2

* Wed Jul 23 2008 Denis Leroy <denis@poolshark.org> - 2.17.1-1
- Update to upstream 2.17.1

* Thu Jul  3 2008 Denis Leroy <denis@poolshark.org> - 2.17.0-1
- Update to unstable branch 2.17

* Sat May 17 2008 Denis Leroy <denis@poolshark.org> - 2.16.2-1
- Update to upstream 2.16.2

* Sat Apr 12 2008 Denis Leroy <denis@poolshark.org> - 2.16.1-1
- Update to upstream 2.16.1, filechooser refcount bugfix

* Wed Mar 12 2008 Denis Leroy <denis@poolshark.org> - 2.16.0-1
- Update to upstream 2.16.0, added --disable-fulldocs

* Tue Feb 12 2008 Denis Leroy <denis@poolshark.org> - 2.15.5-1
- Update to 2.15.5, skipping borked 2.15.4, CHANGES file gone

* Wed Jan 23 2008 Denis Leroy <denis@poolshark.org> - 2.15.2-1
- Update to upstream 2.15.2

* Tue Jan  8 2008 Denis Leroy <denis@poolshark.org> - 2.15.0-1
- Update to 2.15 branch, to follow up with glib2
- Now with giomm goodness

* Sun Nov  4 2007 Denis Leroy <denis@poolshark.org> - 2.14.2-1
- Update to 2.14.2, BRs update

* Fri Sep 14 2007 Denis Leroy <denis@poolshark.org> - 2.14.0-1
- Update to new stable tree 2.14.0

* Thu Sep  6 2007 Denis Leroy <denis@poolshark.org> - 2.13.9-3
- Removed Perl code autogeneration tools (#278191)

* Wed Aug 22 2007 Denis Leroy <denis@poolshark.org> - 2.13.9-2
- License tag update

* Wed Aug  1 2007 Denis Leroy <denis@poolshark.org> - 2.13.9-1
- Update to 2.13.9

* Tue Jul  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.13.6-3
- Rebuild against newest GLib (due to #245141, #245634)

* Fri Jun 22 2007 Denis Leroy <denis@poolshark.org> - 2.13.6-2
- Moved documentation to devhelp directory

* Thu Jun 21 2007 Denis Leroy <denis@poolshark.org> - 2.13.6-1
- Update to unstable 2.13 tree to follow glib2 version

* Mon Apr 30 2007 Denis Leroy <denis@poolshark.org> - 2.12.8-1
- Update to 2.12.8

* Thu Mar 15 2007 Denis Leroy <denis@poolshark.org> - 2.12.7-1
- Update to 2.12.7

* Sun Jan 28 2007 Denis Leroy <denis@poolshark.org> - 2.12.5-1
- Update to 2.12.5, some spec cleanups

* Tue Jan  9 2007 Denis Leroy <denis@poolshark.org> - 2.12.4-1
- Update to 2.12.4, number of bug fixes

* Mon Dec  4 2006 Denis Leroy <denis@poolshark.org> - 2.12.3-1
- Update to 2.12.3
- Added dist tag

* Mon Oct  2 2006 Denis Leroy <denis@poolshark.org> - 2.12.2-1
- Update to 2.12.2

* Mon Aug 28 2006 Denis Leroy <denis@poolshark.org> - 2.12.0-2
- FE6 Rebuild

* Mon Aug 21 2006 Denis Leroy <denis@poolshark.org> - 2.12.0-1
- Update to 2.12.0

* Sun Jun 25 2006 Denis Leroy <denis@poolshark.org> - 2.10.4-1
- Update to 2.10.4

* Sun May  7 2006 Denis Leroy <denis@poolshark.org> - 2.10.1-1
- Update to 2.10.1

* Mon Mar 20 2006 Denis Leroy <denis@poolshark.org> - 2.10.0-1
- Update to 2.10.0, requires newer glib

* Tue Feb 28 2006 Denis Leroy <denis@poolshark.org> - 2.8.4-1
- Update to 2.8.4
- Added optional macro to enable static libs

* Sat Dec 17 2005 Denis Leroy <denis@poolshark.org> - 2.8.3-1
- Update to 2.8.3

* Fri Nov 25 2005 Denis Leroy <denis@poolshark.org> - 2.8.2-1
- Update to 2.8.2
- Disabled static libraries

* Mon Sep 19 2005 Denis Leroy <denis@poolshark.org> - 2.8.0-1
- Upgrade to 2.8.0
- Updated glib2 version dependency

* Fri Sep  2 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 2.6.1-2
- rebuild for gcc-c++-4.0.1-12
  result for GLIBMM_CXX_ALLOWS_STATIC_INLINE_NPOS check changed

* Sat Apr  9 2005 Denis Leroy <denis@poolshark.org> - 2.6.1-1
- Update to version 2.6.1

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Nov 17 2004 Denis Leroy <denis@poolshark.org> - 0:2.4.5-1
- Upgrade to glibmm 2.4.5

* Mon Jun 27 2004 Denis Leroy <denis@poolshark.org> - 0:2.4.4-0.fdr.1
- Upgrade to 2.4.4
- Moved docs to regular directory

* Fri Dec 6 2002 Gary Peck <gbpeck@sbcglobal.net> - 2.0.2-1
- Removed "--without docs" option and simplified the spec file since the
  documentation is included in the tarball now

* Thu Dec 5 2002 Walter H. van Holst <rpm-maintainer@fossiel.xs4all.nl> - 1.0.2
- Removed reference to patch
- Added the documentation files in %files

* Thu Oct 31 2002 Gary Peck <gbpeck@sbcglobal.net> - 2.0.0-gp1
- Update to 2.0.0

* Wed Oct 30 2002 Gary Peck <gbpeck@sbcglobal.net> - 1.3.26-gp3
- Added "--without docs" option to disable DocBook generation

* Sat Oct 26 2002 Gary Peck <gbpeck@sbcglobal.net> - 1.3.26-gp2
- Update to 1.3.26
- Spec file cleanups
- Removed examples from devel package
- Build html documentation (including a Makefile patch)

* Mon Oct 14 2002 Gary Peck <gbpeck@sbcglobal.net> - 1.3.24-gp1
- Initial release of gtkmm2, using gtkmm spec file as base

