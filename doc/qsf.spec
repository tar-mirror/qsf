Summary: Quick Spam Filter
%if %{?_with_static:1}0
Name: qsf-static
%else
Name: qsf
%endif
Version: 1.2.11
Release: 1
License: Artistic 2.0
Group: Development/Tools
Source: http://www.ivarch.com/programs/sources/qsf-1.2.11.tar.bz2
URL: http://www.ivarch.com/programs/qsf.shtml
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%if %{?_with_static:1}0
Obsoletes: qsf
%else
Obsoletes: qsf-static
%endif
Provides: qsf = 1.2.11-1

%description
Quick Spam Filter (qsf) is a small, fast spam filter that works by
learning to recognise the words that are more likely to appear in spam than
non-spam.  It is intended to be used in a procmail recipe to mark email as
being possible spam.

Available rpmbuild rebuild options:
  --without: gdbm mysql sqlite
     --with: static

%prep
%setup -q -n qsf-1.2.11

%build
CFLAGS="$RPM_OPT_FLAGS" sh ./configure \
%if %{?_without_gdbm:1}0
  --without-gdbm \
%endif
%if %{?_without_mysql:1}0
  --without-mysql \
%endif
%if %{?_without_sqlite:1}0
  --without-sqlite \
%endif
%if %{?_with_static:1}0
  --enable-static \
%endif
  --prefix=/usr \
  --infodir=/usr/share/info \
  --mandir=/usr/share/man \
  --sysconfdir=/etc
make %{?_smp_mflags}

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"
[ -e "$RPM_BUILD_ROOT" ] || mkdir -m 755 "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"
chmod 755 "$RPM_BUILD_ROOT"/usr/bin/qsf*

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-, root, root)
/usr/bin/qsf
%docdir /usr/share/man/man1
/usr/share/man/man1/*
%doc README doc/NEWS doc/TODO doc/COPYING doc/postfix-howto extra/*.sh

%changelog
* Sat Jan  3 2015 Andrew Wood <andrew.wood@ivarch.com> 1.2.11-1
- bugfix: Debian #773546 - report error on malformed message (Jameson Graef
- Rollins)
- bugfix: Debian #651881 - X-Spam-Level corruption on non-ASCII spam (Ian
- Zimmerman)
- bugfix: MD5Final now correctly clears context (patch from David Binderman)
- bugfix: removed "DESTDIR" / suffix to fix Cygwin installation
- cleanup: mailbox code consolidated into single file
- cleanup: moved acknowledgements out of manual page
- cleanup: better "rpm" and "srpm" build targets

* Tue Aug 28 2007 Andrew Wood <andrew.wood@ivarch.com> 1.2.7-1
- Changed to Artistic License 2.0.
- Removed "-l" option.

* Sun Feb  4 2007 Andrew Wood <andrew.wood@ivarch.com> 1.2.6-1
- Removed locking from MySQL as it makes it too slow.

* Sun Jan 21 2007 Andrew Wood <andrew.wood@ivarch.com> 1.2.5-1
- Major bugfix in the "list" backend to fix the random deletion of tokens.
- Improved MySQL support.

* Wed Oct 25 2006 Andrew Wood <andrew.wood@ivarch.com> 1.2.1-1
- Concurrent updates now work correctly on all database backends.

* Mon Oct  2 2006 Andrew Wood <andrew.wood@ivarch.com>
- A new database backend called "list". New options to set value of X-Spam
- header, keep a plaintext mapping of hashes to tokens, and maintain a
- deny-list. Allow and deny lists can now list domains as well as individual
- email addresses.

* Mon Aug 14 2006 Andrew Wood <andrew.wood@ivarch.com>
- Code cleanup and fixes for various non-i386-Linux problems.

* Sat Apr  8 2006 Andrew Wood <andrew.wood@ivarch.com>
- Addresses from the Return-Path: header are now also checked against the
- allow-list in addition to those from the From: header.

* Thu Feb  2 2006 Andrew Wood <andrew.wood@ivarch.com>
- Tokenisation fixes for URLs at the start of messages and for nested
- attachments.

* Thu Jul  7 2005 Andrew Wood <andrew.wood@ivarch.com>
- Allow list matching is now case insensitive;
- a btree database's last-modification is updated after any modification;
- the spec file was fixed to work with Fedora Core 4.

* Thu May 12 2005 Andrew Wood <andrew.wood@ivarch.com>
- Tokens now have an age marker;
- additional token types were added;
- the database pruning algorithm was improved;
- the binary tree backend has had some speed enhancements.

* Fri Mar  4 2005 Andrew Wood <andrew.wood@ivarch.com>
- Moved all internal db functions to one file;
- all backends can now be compiled into the same binary;
- some cleanup of code;
- benchmarking has been improved;
- the RPM can now be built with statically linked backends.

* Mon Feb 28 2005 Andrew Wood <andrew.wood@ivarch.com>
- Fixed the documentation of the "--dump" option;
- checked where "--dump" is dumping data to;
- no longer dump large messages in non-filtering mode;
- reporting of database backend in verbose mode.

* Sat Feb 19 2005 Andrew Wood <andrew.wood@ivarch.com>
- A new option to skip short messages was added;
- an option to tune the extent of database pruning was added;
- and the tokeniser was improved.

* Sat Feb  5 2005 Andrew Wood <andrew.wood@ivarch.com>
- Bug fixes when building RPMs, and added support for "rpmbuild --with".

* Sun Sep 26 2004 Andrew Wood <andrew.wood@ivarch.com>
- Code cleanup, and new routines to decode character-encoded headers.

* Wed Sep 22 2004 Andrew Wood <andrew.wood@ivarch.com>
- A new database backend based on SQLite was added.

* Tue Jun 22 2004 Andrew Wood <andrew.wood@ivarch.com>
- A new verbosity option to add errors and information as message headers;
- an option to output stars like SpamAssassin was added;
- the allow-list can be queried using an address read from an email; and
- a system-wide filtering HOWTO was added.

* Tue Apr 27 2004 Andrew Wood <andrew.wood@ivarch.com>
- More explanation of tokenisation, and a new troubleshooting section added
  to the manual.

* Fri Mar 12 2004 Andrew Wood <andrew.wood@ivarch.com>
- Code cleanup, many new filters, and some command line syntax improvements.

* Fri Jan 16 2004 Andrew Wood <andrew.wood@ivarch.com>
- A new option to query and update the allow-list directly was added;
- the spam threshold level can be now altered;
- a second "global" database can now be used; and
- some minor bug fixes were made.

* Mon Jan  5 2004 Andrew Wood <andrew.wood@ivarch.com>
- The tokeniser was improved further to recognise distinct URLs and compress whitespace.
- Additional filters for IP-based URLs and virus attachments were added.

* Sat Dec 27 2003 Andrew Wood <andrew.wood@ivarch.com>
- Minor cosmetic fixes were made for non-Linux systems.
- Speed improvements have been made in the binary tree backend database.

* Fri Nov 14 2003 Andrew Wood <andrew.wood@ivarch.com>
- Added "-mysql" subpackage for optional MySQL backend

* Thu Aug 21 2003 Andrew Wood <andrew.wood@ivarch.com>
- Added package description

* Sat Jan 11 2003 Andrew Wood <andrew.wood@ivarch.com>
- First draft of spec file created
