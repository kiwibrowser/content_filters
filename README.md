<p align="center">
  <img src="https://raw.githubusercontent.com/kiwibrowser/src.next/kiwi/kiwi_logo_circle.svg" alt="KiwiBrowser"
	title="KiwiBrowser" width="200" height="200"/>
 </p>


# Kiwi Browser Content Filters

Source-code for the content filters used to block intrusive ads in Kiwi Browser.

When launched in 2018, Kiwi Browser the only browser (aside Google Chrome) to use the integrated subresource_filter component as a system to remove intrusive ads on websites.

After that, other browsers started to also use this system, so the lists generated by the repository may be compatible with other browsers, including Chrome itself (but this is not guaranteed).

Documentation for subresource_filter: https://chromium.googlesource.com/chromium/src.git/+/main/components/subresource_filter/README.md

In this repository you can configure the lists that are generated.

subresource_filter is an optional component in Kiwi Browser and each list may have its own license.
