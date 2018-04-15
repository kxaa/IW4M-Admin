﻿using SharedLibraryCore.Interfaces;
using System.Collections.Generic;

namespace SharedLibraryCore.Configuration
{
    public class ServerConfiguration : IBaseConfiguration
    {
        public string IPAddress { get; set; }
        public short Port { get; set; }
        public string Password { get; set; }
        public List<string> Rules { get; set; }
        public List<string> AutoMessages { get; set; }
        public bool UseT6MParser { get; set; }

        public IBaseConfiguration Generate()
        {
            UseT6MParser = Utilities.PromptBool("Use T6M parser");
            return this;
        }

        public string Name() => "ServerConfiguration";
    }
}