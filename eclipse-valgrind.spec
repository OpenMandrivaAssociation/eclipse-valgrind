%define src_repo_tag   R0_6_1
%define eclipse_base   %{_libdir}/eclipse
%define install_loc    %{_libdir}/eclipse/dropins/valgrind
%define qualifier      201010081413

# Package in %%{_libdir} but no native code so no debuginfo
%global debug_package %{nil}

Name:           eclipse-valgrind
Version:        0.6.1
Release:        4
Summary:        Valgrind Tools Integration for Eclipse

Group:          Development/Java
License:        EPL
URL:            http://www.eclipse.org/linuxtools/projectPages/valgrind
# Fetched using: sh %{name}-fetch-src.sh %{src_repo_tag}
Source0:        %{name}-fetched-src-%{src_repo_tag}.tar.bz2
Source1:        %{name}-fetch-src.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#No CDT on ppc64
ExcludeArch: ppc64

BuildRequires: java-devel >= 1.5.0
BuildRequires: eclipse-cdt >= 0:7.0.0
BuildRequires: eclipse-linuxprofilingframework >= 0.6.0
BuildRequires: eclipse-birt >= 2.5
BuildRequires: eclipse-pde >= 0:3.6.0
Requires: eclipse-platform >= 0:3.6.0
Requires: eclipse-cdt >= 0:7.0.0
Requires: eclipse-linuxprofilingframework >= 0.6.0
Requires: eclipse-birt >= 2.5
Requires: valgrind >= 3.3.0

%description
This package for Eclipse allows users to launch their C/C++ Development Tools
projects using the Valgrind tool suite and presents the results in the IDE. 

%prep
%setup -q -n %{name}-fetched-src-%{src_repo_tag}

%build
%{eclipse_base}/buildscripts/pdebuild \
    -f org.eclipse.linuxtools.valgrind \
    -d "cdt linuxprofilingframework emf rhino birt" \
    -a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier}"

%install
%{__rm} -rf %{buildroot}
install -d -m 755 %{buildroot}%{install_loc}

%{__unzip} -q -d %{buildroot}%{install_loc} \
     build/rpmBuild/org.eclipse.linuxtools.valgrind.zip 

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{install_loc}
%doc org.eclipse.linuxtools.valgrind-feature/epl-v10.html

