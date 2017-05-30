query1 = {"$text": {"$search": "smallestVersion"}}

query2 = {"$and": [
    {"classes.name": "DiscoveryNodes.class"},
    {"$text": {"$search": "smallestVersion"}}
]}

query3 = {"$and": [
    {"package": "org.elasticsearch.cluster.node"},
    {"classes.name": "DiscoveryNodes.class"},
    {"$text": {"$search": "smallestVersion"}}
]}

query4 = {"$text": {"$search": "toString"}}

query5 = {"$and": [
    {"classes.name": "ProxyDiagnostics.class"},
    {"$text": {"$search": "toString"}}
]}

query6 = {"$and": [
    {"package": "org.apache.tools.ant.util.java15"},
    {"classes.name": "ProxyDiagnostics.class"},
    {"$text": {"$search": "toString"}}
]}

query7 = {"$and": [
    {"classes.name": "DiscoveryNode.class"},
    {"classes.name": "DiscoveryNodes.class"},
    {"classes.name": "DiscoveryNodeService.class"},
    {"classes.name": "DiscoveryNodeFilters.class"},
    {"$text": {"$search": "\"localNode\" "
                          "\"clientNode\" "
                          "\"masterNode\" "
                          "\"address\" "
                          "\"getNodes\" "
                          "\"getMasterNodes\" "
                          "\"getLocalNode\" "
                          "\"readFrom\" "
                          "\"addCustomAttributeProvider\" "
                          "\"buildAttributes\" "
                          "\"buildFromSettings\" "
                          "\"buildFromKeyValue\" "
                          "\"match\" "
                          "\"toString\" "}}
]}

query8 = {"$and": [
    {"classes.name": "ArrayUtils.class"},
    {"classes.name": "BitField.class"},
    {"classes.name": "BooleanUtils.class"},
    {"classes.name": "CharUtils.class"},
    {"classes.name": "ClassUtils.class"},
    {"classes.name": "IntHashMap.class"},
    {"classes.name": "LocaleUtils.class"},
    {"classes.name": "NotImplementedException.class"},
    {"$text": {"$search": "\"toString\" "
                          "\"hashCode\" "
                          "\"toMap\" "
                          "\"clone\" "
                          "\"subarray\" "
                          "\"isSameLength\" "
                          "\"indexOf\" "
                          "\"toPrimitive\" "
                          "\"getValue\" "
                          "\"getShortValue\" "
                          "\"getRawValue\" "
                          "\"getShortRawValue\" "
                          "\"isSet\" "
                          "\"isAllSet\" "
                          "\"setValue\" "
                          "\"setShortValue\" "
                          "\"negate\" "
                          "\"isTrue\" "
                          "\"isNotTrue\" "
                          "\"isFalse\" "
                          "\"isNotFalse\" "
                          "\"toBooleanObject\" "
                          "\"toBoolean\" "
                          "\"toBooleanDefaultIfNull\" "
                          "\"toCharacterObject\" "
                          "\"toChar\" "
                          "\"toIntValue\" "
                          "\"unicodeEscaped\" "
                          "\"isAscii\" "
                          "\"isAsciiPrintable\" "
                          "\"isAsciiControl\" "
                          "\"isAsciiAlpha\" "
                          "\"getShortClassName\" "
                          "\"getPackageName\" "
                          "\"getAllSuperclasses\" "
                          "\"getAllInterfaces\" "
                          "\"convertClassNamesToClasses\" "
                          "\"convertClassesToClassNames\" "
                          "\"isAssignable\" "
                          "\"primitiveToWrapper\" "
                          "\"size\" "
                          "\"isEmpty\" "
                          "\"contains\" "
                          "\"containsValue\" "
                          "\"containsKey\" "
                          "\"get\" "
                          "\"put\" "
                          "\"remove\" "
                          "\"LocaleUtils\" "
                          "\"toLocale\" "
                          "\"localeLookupList\" "
                          "\"availableLocaleList\" "
                          "\"availableLocaleSet\" "
                          "\"isAvailableLocale\" "
                          "\"languagesByCountry\" "
                          "\"countriesByLanguage\" "
                          "\"getCause\" "
                          "\"getMessage\" "
                          "\"getMessages\" "
                          "\"getThrowable\" "
                          "\"getThrowableCount\" "
                          "\"getThrowables\" "
                          "\"indexOfThrowable\" "
                          "\"printStackTrace\" "}}
]}

query9 = {"$and": [
    {"classes.name": "NonExisting.class"},
    {"classes.name": "BitField.class"},
    {"classes.name": "BooleanUtils.class"},
    {"classes.name": "CharUtils.class"},
    {"classes.name": "ClassUtils.class"},
    {"classes.name": "IntHashMap.class"},
    {"classes.name": "LocaleUtils.class"},
    {"classes.name": "NotImplementedException.class"},
    {"$text": {"$search": "\"toString\" "
                          "\"hashCode\" "
                          "\"toMap\" "
                          "\"clone\" "
                          "\"subarray\" "
                          "\"isSameLength\" "
                          "\"indexOf\" "
                          "\"toPrimitive\" "
                          "\"getValue\" "
                          "\"getShortValue\" "
                          "\"getRawValue\" "
                          "\"getShortRawValue\" "
                          "\"isSet\" "
                          "\"isAllSet\" "
                          "\"setValue\" "
                          "\"setShortValue\" "
                          "\"negate\" "
                          "\"isTrue\" "
                          "\"isNotTrue\" "
                          "\"isFalse\" "
                          "\"isNotFalse\" "
                          "\"toBooleanObject\" "
                          "\"toBoolean\" "
                          "\"toBooleanDefaultIfNull\" "
                          "\"toCharacterObject\" "
                          "\"toChar\" "
                          "\"toIntValue\" "
                          "\"unicodeEscaped\" "
                          "\"isAscii\" "
                          "\"isAsciiPrintable\" "
                          "\"isAsciiControl\" "
                          "\"isAsciiAlpha\" "
                          "\"getShortClassName\" "
                          "\"getPackageName\" "
                          "\"getAllSuperclasses\" "
                          "\"getAllInterfaces\" "
                          "\"convertClassNamesToClasses\" "
                          "\"convertClassesToClassNames\" "
                          "\"isAssignable\" "
                          "\"primitiveToWrapper\" "
                          "\"size\" "
                          "\"isEmpty\" "
                          "\"contains\" "
                          "\"containsValue\" "
                          "\"containsKey\" "
                          "\"get\" "
                          "\"put\" "
                          "\"remove\" "
                          "\"LocaleUtils\" "
                          "\"toLocale\" "
                          "\"localeLookupList\" "
                          "\"availableLocaleList\" "
                          "\"availableLocaleSet\" "
                          "\"isAvailableLocale\" "
                          "\"languagesByCountry\" "
                          "\"countriesByLanguage\" "
                          "\"getCause\" "
                          "\"getMessage\" "
                          "\"getMessages\" "
                          "\"getThrowable\" "
                          "\"getThrowableCount\" "
                          "\"getThrowables\" "
                          "\"indexOfThrowable\" "
                          "\"printStackTrace\" "}}
]}

mongo_query_list = [query1, query2, query3, query4, query5, query6, query7, query8, query9]
