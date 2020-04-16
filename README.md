# Is it Friday?

## Table of Contents
<!-- vim-markdown-toc GitLab -->

* [What does this do?](#what-does-this-do)
* [But why?](#but-why)
* [Limitations](#limitations)
* [I don't want to wait!](#i-dont-want-to-wait)
* [What's that `openshift` directory?](#whats-that-openshift-directory)
* [Contributing](#contributing)

<!-- vim-markdown-toc -->

## What does this do?

This web app does thing, and on thing only, answer that all important question
that gets asked in (home-)offices around the world every single day: **„Is it
Friday?”**.

It answers the question with a simple yes or no, and it even shows you how many
more nights of sleep you need before it will be Friday.

## But why?

I needed a simple application to demo and test (Tekton) pipelines that use
Source-to-Image (S2I) builds. This application, with its small dependencies and
quick build times firs the bill perfectly, and it's nicer than a static webpage
test.

## Limitations

This app is not very sophisticated. It looks at the current server time to
figure out the current weekday, and works from there. If you want something
that works in your local timezone I would suggest something else.

## I don't want to wait!

Add `?nts=0` to the end of the URL. Replace `0` with how many nights you wish
it would be until Friday.

## What's that `openshift` directory?

It's a directory with [kustomize](https://kustomize.io) manifests for deploying this app on OpenShift. It is used with my [Tekton Tutorial](https://gitlab.com/wanderb/tekton-tutorial).

## Contributing

I'll take contributions, just create a merge request for me.
