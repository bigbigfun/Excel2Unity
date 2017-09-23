
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ConfigUtil
{
    public static List<int> ParseListInt(string data)
    {
        return JsonUtility.FromJson<List<int>>(data);
    }

    public static List<float> ParseListFloat(string data)
    {
        return JsonUtility.FromJson<List<float>>(data);
    }

    public static List<string> ParseListString(string data)
    {
        return JsonUtility.FromJson<List<string>>(data);
    }

    public static Dictionary<int, int> ParseDictIntInt(string data)
    {
        return JsonUtility.FromJson<Dictionary<int, int>>(data);
    }

    public static Dictionary<int, float> ParseDictIntFloat(string data)
    {
        return JsonUtility.FromJson<Dictionary<int, float>>(data);
    }

    public static Dictionary<int, string> ParseDictIntString(string data)
    {
        return JsonUtility.FromJson<Dictionary<int, string>>(data);
    }

    public static Dictionary<string, int> ParseDictStringInt(string data)
    {
        return JsonUtility.FromJson<Dictionary<string, int>>(data);
    }

    public static Dictionary<string, float> ParseDictStringFloat(string data)
    {
        return JsonUtility.FromJson<Dictionary<string, float>>(data);
    }

    public static Dictionary<string, string> ParseDictStringString(string data)
    {
        return JsonUtility.FromJson<Dictionary<string, string>>(data);
    }
}
