//
//  helloWorldApp.swift
//  helloWorld
//
//  Created by Aslan on 20.01.2024.
//

import SwiftUI

@main
struct helloWorldApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: helloWorldDocument()) { file in
            ContentView(document: file.$document)
        }
    }
}
