// Generated from /home/jordi/Escritorio/Jordi/q6/lp/lp_hinner/hm.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class hmLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		OPER=1, LPAR=2, RPAR=3, ARROW=4, CBAR=5, PP=6, ID=7, TYPE=8, NUM=9, WS=10;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"OPER", "LPAR", "RPAR", "ARROW", "CBAR", "PP", "ID", "TYPE", "NUM", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "'('", "')'", "'->'", "'\\'", "'::'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "OPER", "LPAR", "RPAR", "ARROW", "CBAR", "PP", "ID", "TYPE", "NUM", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public hmLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "hm.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\nI\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0003\u0000\"\b\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0006\u0001\u0006\u0005\u00062\b\u0006\n\u0006\f\u00065\t\u0006\u0001"+
		"\u0007\u0001\u0007\u0005\u00079\b\u0007\n\u0007\f\u0007<\t\u0007\u0001"+
		"\b\u0004\b?\b\b\u000b\b\f\b@\u0001\t\u0004\tD\b\t\u000b\t\f\tE\u0001\t"+
		"\u0001\t\u0000\u0000\n\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004"+
		"\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0001\u0000\u0005"+
		"\u0001\u0000az\u0002\u0000AZaz\u0001\u0000AZ\u0001\u000009\u0003\u0000"+
		"\t\n\r\r  O\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000"+
		"\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000"+
		"\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000"+
		"\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000"+
		"\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000"+
		"\u0001!\u0001\u0000\u0000\u0000\u0003#\u0001\u0000\u0000\u0000\u0005%"+
		"\u0001\u0000\u0000\u0000\u0007\'\u0001\u0000\u0000\u0000\t*\u0001\u0000"+
		"\u0000\u0000\u000b,\u0001\u0000\u0000\u0000\r/\u0001\u0000\u0000\u0000"+
		"\u000f6\u0001\u0000\u0000\u0000\u0011>\u0001\u0000\u0000\u0000\u0013C"+
		"\u0001\u0000\u0000\u0000\u0015\u0016\u0005(\u0000\u0000\u0016\u0017\u0005"+
		"*\u0000\u0000\u0017\"\u0005)\u0000\u0000\u0018\u0019\u0005(\u0000\u0000"+
		"\u0019\u001a\u0005/\u0000\u0000\u001a\"\u0005)\u0000\u0000\u001b\u001c"+
		"\u0005(\u0000\u0000\u001c\u001d\u0005+\u0000\u0000\u001d\"\u0005)\u0000"+
		"\u0000\u001e\u001f\u0005(\u0000\u0000\u001f \u0005-\u0000\u0000 \"\u0005"+
		")\u0000\u0000!\u0015\u0001\u0000\u0000\u0000!\u0018\u0001\u0000\u0000"+
		"\u0000!\u001b\u0001\u0000\u0000\u0000!\u001e\u0001\u0000\u0000\u0000\""+
		"\u0002\u0001\u0000\u0000\u0000#$\u0005(\u0000\u0000$\u0004\u0001\u0000"+
		"\u0000\u0000%&\u0005)\u0000\u0000&\u0006\u0001\u0000\u0000\u0000\'(\u0005"+
		"-\u0000\u0000()\u0005>\u0000\u0000)\b\u0001\u0000\u0000\u0000*+\u0005"+
		"\\\u0000\u0000+\n\u0001\u0000\u0000\u0000,-\u0005:\u0000\u0000-.\u0005"+
		":\u0000\u0000.\f\u0001\u0000\u0000\u0000/3\u0007\u0000\u0000\u000002\u0007"+
		"\u0001\u0000\u000010\u0001\u0000\u0000\u000025\u0001\u0000\u0000\u0000"+
		"31\u0001\u0000\u0000\u000034\u0001\u0000\u0000\u00004\u000e\u0001\u0000"+
		"\u0000\u000053\u0001\u0000\u0000\u00006:\u0007\u0002\u0000\u000079\u0007"+
		"\u0001\u0000\u000087\u0001\u0000\u0000\u00009<\u0001\u0000\u0000\u0000"+
		":8\u0001\u0000\u0000\u0000:;\u0001\u0000\u0000\u0000;\u0010\u0001\u0000"+
		"\u0000\u0000<:\u0001\u0000\u0000\u0000=?\u0007\u0003\u0000\u0000>=\u0001"+
		"\u0000\u0000\u0000?@\u0001\u0000\u0000\u0000@>\u0001\u0000\u0000\u0000"+
		"@A\u0001\u0000\u0000\u0000A\u0012\u0001\u0000\u0000\u0000BD\u0007\u0004"+
		"\u0000\u0000CB\u0001\u0000\u0000\u0000DE\u0001\u0000\u0000\u0000EC\u0001"+
		"\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000FG\u0001\u0000\u0000\u0000"+
		"GH\u0006\t\u0000\u0000H\u0014\u0001\u0000\u0000\u0000\u0006\u0000!3:@"+
		"E\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}