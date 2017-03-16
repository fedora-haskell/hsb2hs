# https://fedoraproject.org/wiki/Packaging:Haskell

%global ghc_without_dynamic 1

# nothing to see here
%global debug_package %{nil}

Name:           hsb2hs
Version:        0.3.1
Release:        2%{?dist}
Summary:        Preprocesses a file, adding blobs from files as string literals

License:        BSD
Url:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
#BuildRequires:  ghc-preprocessor-tools-devel
# End cabal-rpm deps
BuildRequires:  cabal-install

%description
Hsb2hs is a preprocessor that allows you to include the contents of files as
string literals in your Haskell programs and libraries. It is an alternative to
file-embed for those who do not want to rely on Template Haskell.


%prep
%setup -q


%build
%global cabal cabal
[ -d "$HOME/.cabal" ] || %cabal update
%cabal install --only-dependencies
%cabal configure --prefix=%{_prefix} --libdir=%{_libdir} --docdir=%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}
%cabal build


%install
%ghc_bin_install


%files
%doc LICENSE
%{_bindir}/%{name}


%changelog
* Wed Feb  1 2017 Jens Petersen <petersen@redhat.com> - 0.3.1-2
- rebuild

* Sun Oct 04 2015 Jens Petersen <petersen@redhat.com> - 0.3.1-1
- update to 0.3.1

* Tue Jun 23 2015 Jens Petersen <petersen@redhat.com> - 0.3-1
- update to 0.3

* Thu Dec 25 2014 Jens Petersen <petersen@redhat.com> - 0.1-2
- run cabal update if no ~/.cabal

* Thu Jan 30 2014 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.1-1
- spec file generated by cabal-rpm-0.8.7
