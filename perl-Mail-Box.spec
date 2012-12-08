%define	upstream_name    Mail-Box
%define upstream_version 2.099

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Mail-folder manager API
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Mail/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-File-Remove
BuildRequires:	perl-HTML-Format
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-Mail-IMAPClient
BuildRequires:	perl-Mail-MboxParser
BuildRequires:	perl-Mail-SpamAssassin
BuildRequires:	perl-MailTools
BuildRequires:	perl-MIME-tools
BuildRequires:	perl-MIME-Types
BuildRequires:	perl-Object-Realize-Later
BuildRequires:	perl-User-Identity
BuildRequires:	perl-devel

BuildArch:	noarch

Requires:	perl(Object::Realize::Later)
Provides:	perl(Mail::Message::Construct)

%description
Mail::Box is a Perl CPAN package that can be used to handle and manage E-mail
messages, mail boxes, and folders of many types.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%install
%makeinstall_std

# fix permissions
find %{buildroot} -type f -exec chmod 0644 {} \;
find %{buildroot} -type d -exec chmod 0755 {} \;

# remove unused file
rm -f %{buildroot}%{perl_vendorlib}/Mail/Makefile.PL

%files
%doc ChangeLog INSTALL LICENSE README* TODO.v2
%{_mandir}/*/*
%{perl_vendorlib}/Mail


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.99.0-3mdv2012.0
+ Revision: 765396
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 2.099

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.98.0-2
+ Revision: 667247
- mass rebuild

* Fri Mar 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.98.0-1
+ Revision: 646338
- update to new version 2.098

* Mon Jan 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.97.0-1
+ Revision: 634485
- update to new version 2.097

* Sat Dec 18 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.96.0-1mdv2011.0
+ Revision: 622845
- update to new version 2.096

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 2.95.0-2mdv2011.0
+ Revision: 564739
- rebuild for perl 5.12.1

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 2.95.0-1mdv2011.0
+ Revision: 552412
- update to 2.095

* Tue Apr 06 2010 Jérôme Quelin <jquelin@mandriva.org> 2.94.0-1mdv2010.1
+ Revision: 532152
- update to 2.094

  + Shlomi Fish <shlomif@mandriva.org>
    - Convert to a better description.

* Mon Dec 28 2009 Jérôme Quelin <jquelin@mandriva.org> 2.93.0-1mdv2010.1
+ Revision: 483042
- update to 2.093

* Sat Nov 21 2009 Jérôme Quelin <jquelin@mandriva.org> 2.92.0-1mdv2010.1
+ Revision: 467881
- update to 2.092

* Mon Sep 07 2009 Jérôme Quelin <jquelin@mandriva.org> 2.91.0-1mdv2010.0
+ Revision: 432396
- update to 2.091

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.090-1mdv2010.0
+ Revision: 383527
- update to new version 2.090

* Sat May 02 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.089-1mdv2010.0
+ Revision: 370489
- update to new version 2.089

* Wed Mar 25 2009 Michael Scherer <misc@mandriva.org> 2.088-2mdv2009.1
+ Revision: 360973
- fix missing Requires

* Fri Mar 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.088-1mdv2009.1
+ Revision: 359060
- update to new version 2.088

* Wed Feb 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.087-1mdv2009.1
+ Revision: 337658
- update to new version 2.087

* Sun Dec 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.086-1mdv2009.1
+ Revision: 314251
- update to new version 2.086

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.084-1mdv2009.1
+ Revision: 292198
- update to new version 2.084

* Fri Sep 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.083-1mdv2009.0
+ Revision: 281737
- new version

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.082-2mdv2009.0
+ Revision: 265369
- rebuild early 2009.0 package (before pixel changes)

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.082-1mdv2009.0
+ Revision: 201857
- update to new version 2.082

* Tue Feb 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.081-1mdv2008.1
+ Revision: 175332
- update to new version 2.081

* Tue Jan 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.080-1mdv2008.1
+ Revision: 156178
- update to new version 2.080
- update to new version 2.080

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.079-1mdv2008.1
+ Revision: 113872
- update to new version 2.079

* Sun Nov 11 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.078-1mdv2008.1
+ Revision: 107977
- update to new version 2.078

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.076-1mdv2008.1
+ Revision: 104560
- update to new version 2.076

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.075-1mdv2008.1
+ Revision: 97512
- update to new version 2.075

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.073-1mdv2008.0
+ Revision: 56104
- new version

* Tue Jul 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.072-1mdv2008.0
+ Revision: 47697
- update to new version 2.072

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 2.070-1mdv2008.0
+ Revision: 20263
- 2.070
- disable test, don't start

* Fri Apr 27 2007 Oden Eriksson <oeriksson@mandriva.com> 2.065-2mdv2008.0
+ Revision: 18584
- rebuild


* Tue Mar 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.065-1mdk
- New release

* Mon Nov 07 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.063-1mdk
- 2.063

* Wed Sep 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.062-1mdk
- New release 2.062
- rpmbuildupdate aware
- spec cleanup

* Fri Jul 08 2005 Andreas Hasenack <andreas@mandriva.com> 2.061-1mdk
- packaged for Mandriva

