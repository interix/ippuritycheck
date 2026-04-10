---
name: apple-file-providers
description: Implement and maintain file provider extensions for apps on Apple operating systems.
license: MIT
metadata: 
    author: i2h3
---

# Apple File Providers

Production-ready code and expert guidance about the file provider framework by Apple for AI.

## Concurrency

- Take into consideration that method calls from the file provider framework are on an arbitrary queue and may be concurrent. Ensure thread safety in your code.
- Always prefer to use `await` and `async` functions for asynchronous operations instead of completion handlers.
- Bridge completion handler patterns required by the file provider framework (in example `item(for:request:completionHandler:)` on `NSFileProviderReplicatedExtension`) to a `Task` which then calls `async` and `await` code.

## Data Management

- A file provider domain should always use a unique life time identifier based on a `UUID` for itself. Never reuse a previously used `UUID` for a newly added file provider domain. This avoids problems with stale data.
- File provider items should always use a unique identifier based on a `UUID` to identify themselves. Never reuse a previously used `UUID` for a newly created file provider item. This avoids problems with stale data.
- If file provider items have a unique identifier for the remote item they represent, then that identifier must be stored separately and associated with the local `UUID` of the file provider item. The remote identifier might outlive the local file provider domain identifier or file provider item identifier. This is an additional safety measure to avoid problems with stale data.
- If a file provider extension persists data locally, it should use the sandbox container of the file provider extension by default.
- If a file provider extension persists data locally, it should use a dedicated directory for each file provider domain to store its data.
- Data models should always be value types, immutable and conform to `Sendable`.
- Use a dedicated type to implement `NSFileProviderItem` protocol.
- If a file provider item is deleted on the local device, its record must be retained and marked as deleted until the the deletion could actually be performed on the remote item.
- If a file provider item is detected as deleted on the remote end, it must also be deleted from the local metadata persistence but only after it has been reported to the file provider framework as deleted. This is required to properly report deletions to the file provider framework and avoid problems with stale data.

## User Interface

- Finder displays the name of the app which manages a file provider domain in the Finder sidebar, assuming there is only one file provider domain by an app. In case there is more than one file provider domain by an app, then Finder displays the app name and the programmatically defined display name of the file provider domain, both separated by a hyphen.
- Updating the display name of a file provider domain requires a NSFileProviderDomain object with the same identifier to be added again through the NSFileProviderManager.

## Error Reporting

- When implementing `NSFileProviderEnumerating`, the `func enumerator(for containerItemIdentifier: NSFileProviderItemIdentifier, request: NSFileProviderRequest) throws -> any NSFileProviderEnumerator` method must `throw NSFileProviderError(.noSuchItem)` if the requested `containerItemIdentifier` is not a system defined container identifier like `NSRootContainerItemIdentifier` or does not exist. This is required to properly report errors to the file provider framework and avoid problems with stale data.

## Troubleshooting

- Use the `fileproviderctl` command line tool to troubleshoot and debug your file provider extension. It allows you to inspect the state of your file provider domains, items, and operations.