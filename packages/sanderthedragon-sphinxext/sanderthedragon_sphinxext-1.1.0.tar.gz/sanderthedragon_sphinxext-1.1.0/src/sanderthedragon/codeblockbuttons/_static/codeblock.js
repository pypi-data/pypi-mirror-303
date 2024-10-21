/*
 * SPDX-FileCopyrightText: 2021-2024 SanderTheDragon <sanderthedragon@zoho.com>
 *
 * SPDX-License-Identifier: MIT
 */

const codeblock = {
    ids: [],

    // Generate an unique ID
    generateID: () => {
        const id = Math.random().toString(36).substr(2);
        if (codeblock.ids.includes(id)) {
            return codeblock.generateID();
        }

        codeblock.ids.push(id);

        return id;
    },

    // From "https://tablericons.com", licensed under MIT
    icons: {
        "view":         "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJpY29uLXRhYmxlciBpY29uLXRhYmxlci1jb2RlIiB2aWV3Qm94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2U9IiMwMDAwMDAiIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+CiAgPHBhdGggc3Ryb2tlPSJub25lIiBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIi8+CiAgPHBvbHlsaW5lIHBvaW50cz0iNyA4IDMgMTIgNyAxNiIgLz4KICA8cG9seWxpbmUgcG9pbnRzPSIxNyA4IDIxIDEyIDE3IDE2IiAvPgogIDxsaW5lIHgxPSIxNCIgeTE9IjQiIHgyPSIxMCIgeTI9IjIwIiAvPgo8L3N2Zz4=",
        "copy":         "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJpY29uLXRhYmxlciBpY29uLXRhYmxlci1jb3B5IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2U9IiMwMDAwMDAiIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+CiAgPHBhdGggc3Ryb2tlPSJub25lIiBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIi8+CiAgPHJlY3QgeD0iOCIgeT0iOCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiByeD0iMiIgLz4KICA8cGF0aCBkPSJNMTYgOHYtMmEyIDIgMCAwIDAgLTIgLTJoLThhMiAyIDAgMCAwIC0yIDJ2OGEyIDIgMCAwIDAgMiAyaDIiIC8+Cjwvc3ZnPg==",
        "copy-error":   "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJpY29uLXRhYmxlciBpY29uLXRhYmxlci1jbGlwYm9hcmQteCIgdmlld0JveD0iMCAwIDI0IDI0IiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlPSIjMDAwMDAwIiBmaWxsPSJub25lIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPgogIDxwYXRoIHN0cm9rZT0ibm9uZSIgZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogIDxwYXRoIGQ9Ik05IDVoLTJhMiAyIDAgMCAwIC0yIDJ2MTJhMiAyIDAgMCAwIDIgMmgxMGEyIDIgMCAwIDAgMiAtMnYtMTJhMiAyIDAgMCAwIC0yIC0yaC0yIiAvPgogIDxyZWN0IHg9IjkiIHk9IjMiIHdpZHRoPSI2IiBoZWlnaHQ9IjQiIHJ4PSIyIiAvPgogIDxwYXRoIGQ9Ik0xMCAxMmw0IDRtMCAtNGwtNCA0IiAvPgo8L3N2Zz4=",
        "copy-success": "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJpY29uLXRhYmxlciBpY29uLXRhYmxlci1jbGlwYm9hcmQtY2hlY2siIHZpZXdCb3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0iIzAwMDAwMCIgZmlsbD0ibm9uZSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj4KICA8cGF0aCBzdHJva2U9Im5vbmUiIGQ9Ik0wIDBoMjR2MjRIMHoiIGZpbGw9Im5vbmUiLz4KICA8cGF0aCBkPSJNOSA1aC0yYTIgMiAwIDAgMCAtMiAydjEyYTIgMiAwIDAgMCAyIDJoMTBhMiAyIDAgMCAwIDIgLTJ2LTEyYTIgMiAwIDAgMCAtMiAtMmgtMiIgLz4KICA8cmVjdCB4PSI5IiB5PSIzIiB3aWR0aD0iNiIgaGVpZ2h0PSI0IiByeD0iMiIgLz4KICA8cGF0aCBkPSJNOSAxNGwyIDJsNCAtNCIgLz4KPC9zdmc+"
    },

    // Set a base64 encoded icon
    setImage: (element, ico) => {
        let icon = element.querySelector(`:scope > div.cb-icon`);
        if (icon == null) {
            icon = document.createElement("div");
            icon.classList.add("cb-icon");

            element.appendChild(icon);
        }

        icon.innerHTML = atob(cb_icons[ico] || codeblock.icons[ico]);
    },

    // Set a tooltip
    setTooltip: (element, text) => {
        let tooltip = element.querySelector(":scope > span.cb-tooltip");
        if (tooltip == null) {
            tooltip = document.createElement("span");
            tooltip.classList.add("cb-tooltip");

            element.appendChild(tooltip);
        }

        tooltip.innerHTML = text;
    },

    // Add controls to a code block
    addControls: (element) => {
        const hasClass = (cls) => {
            return element.parentElement.classList.contains(cls);
        }

        element.id = `_${codeblock.generateID()}`;

        // Force the default to start with `cbd-`
        if (!cb_default.startsWith("cbd-")) {
            // Add the modified default class
            const modified = "cbd-" + cb_default.split("-").pop();
            element.parentElement.classList.add(modified);
        }
        else {
            // Add the default class
            element.parentElement.classList.add(cb_default);
        }

        // Add nothing to code blocks with the `cb-none` class
        if (element.parentElement.classList.contains("cb-none")) {
            return;
        }

        // Set hidden by default, if enabled
        if (cb_hidden) {
            element.parentElement.classList.add("cbd-hidden");
        }

        // Add the transition class, if enabled
        if (cb_transitions) {
            element.parentElement.classList.add("cb-transition");
        }

        // Add the copy button, if needed
        if (((hasClass("cbd-none") || hasClass("cbd-copy"))
                && (hasClass("cb-all") || hasClass("cb-copy")))
            || ((hasClass("cbd-all") || hasClass("cbd-copy"))
                && !hasClass("cb-nocopy"))) {
            let copyButton = document.createElement("div");
            copyButton.classList.add("cb-button");
            copyButton.id = "cb-copy";
            copyButton.setAttribute("data-clipboard-target",
                                    `#${element.id} > pre`);

            codeblock.setImage(copyButton, "copy");
            codeblock.setTooltip(copyButton, "Copy");

            element.appendChild(copyButton);
        }

        // Add the view button, if needed
        if (((hasClass("cbd-none") || hasClass("cbd-copy"))
                && (hasClass("cb-all") || hasClass("cb-view")))
            || ((hasClass("cbd-all") || hasClass("cbd-view"))
                && !hasClass("cb-noview"))) {
            let viewButton = document.createElement("div");
            viewButton.classList.add("cb-button");
            viewButton.id = "cb-view";
            viewButton.setAttribute("data-view-id", element.id);

            codeblock.setImage(viewButton, "view");
            codeblock.setTooltip(viewButton, "View");

            element.appendChild(viewButton);

            // Add handler for view buttons
            element.addEventListener("click", (event) => {
                let target = event.target;
                while (target && target.id != "cb-view") {
                    target = target.parentElement;
                }

                if (target == null) {
                    return;
                }

                // Find the language from the classes for the mime type
                let language = undefined;
                const id = target.getAttribute("data-view-id");
                const element = document.getElementById(id);
                element.parentElement.classList.forEach((cls) => {
                    if (!language && cls.startsWith("highlight-")) {
                        language = cls.substr(cls.indexOf("-") + 1);
                    }
                });

                const mimetype = cb_mimes[language] || "text/plain";

                // Create a blob from the content and then open it
                const data = element.querySelector("pre").innerText;
                const file = new Blob([ data ], { type: mimetype });
                window.open(URL.createObjectURL(file));
            });
        }

        // Make the scroll area large enough to not overlay the code
        const buttonCount = element.getElementsByClassName("cb-button").length;
        if (buttonCount > 0) {
            const position = element.innerHTML.indexOf('\n');
            element.innerHTML = element.innerHTML.slice(0, position)
                                + `<span class="cb-pad cb-pad-${buttonCount}">`
                                + `</span>`
                                + element.innerHTML.slice(position);
        }
    },

    // Reset the copy button from success (or error) to normal
    resetCopyOnLeave: (element) => {
        element.addEventListener("mouseleave", function _rc() {
            codeblock.setImage(element, "copy");
            setTimeout(() => {
                codeblock.setTooltip(element, "Copy")
            }, 50); // After fade out

            element.removeEventListener("mouseleave", _rc);
        });
    },

    initialize: () => {
        // Iterate over all code blocks
        document.querySelectorAll("div.highlight").forEach((element) => {
            codeblock.addControls(element);
        });

        // Create an instance of `ClipboardJS` for `cb-button`s
        const clipboard = new ClipboardJS("div.cb-button#cb-copy");

        clipboard.on("success", (event) => {
            event.clearSelection();

            const element = event.trigger;
            codeblock.setImage(element, "copy-success");
            codeblock.setTooltip(element, "Copied");
            codeblock.resetCopyOnLeave(element);
        });

        clipboard.on("error", (event) => {
            const element = event.trigger;
            codeblock.setImage(element, "copy-error");
            codeblock.setTooltip(element, "Failed");
            codeblock.resetCopyOnLeave(element);
        });
    }
}

document.addEventListener("DOMContentLoaded", codeblock.initialize);
