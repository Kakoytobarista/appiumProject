//
//  ContentView.swift
//  helloWorld
//
//  Created by Aslan on 20.01.2024.
//

import SwiftUI

struct ContentView: View {
    @Binding var document: helloWorldDocument

    var body: some View {
        TextEditor(text: $document.text)
            .accessibility(identifier: "inputField")
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView(document: .constant(helloWorldDocument()))
    }
}
