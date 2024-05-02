// Generated from /home/jordi/Escritorio/Jordi/q6/lp/lp_hinner/hm.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class hmParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PLUS=1, MINUS=2, MUL=3, DIV=4, LPAR=5, RPAR=6, ARROW=7, CBAR=8, ID=9, 
		NUM=10, WS=11;
	public static final int
		RULE_root = 0, RULE_stmts = 1, RULE_stmt = 2, RULE_lam = 3, RULE_apl = 4, 
		RULE_expr = 5, RULE_oper = 6;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "stmts", "stmt", "lam", "apl", "expr", "oper"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'->'", "'\\'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PLUS", "MINUS", "MUL", "DIV", "LPAR", "RPAR", "ARROW", "CBAR", 
			"ID", "NUM", "WS"
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

	@Override
	public String getGrammarFileName() { return "hm.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public hmParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RootContext extends ParserRuleContext {
		public StmtsContext stmts() {
			return getRuleContext(StmtsContext.class,0);
		}
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(14);
			stmts();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StmtsContext extends ParserRuleContext {
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public StmtsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmts; }
	}

	public final StmtsContext stmts() throws RecognitionException {
		StmtsContext _localctx = new StmtsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stmts);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(17); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(16);
				stmt();
				}
				}
				setState(19); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 1824L) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StmtContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AplContext apl() {
			return getRuleContext(AplContext.class,0);
		}
		public LamContext lam() {
			return getRuleContext(LamContext.class,0);
		}
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_stmt);
		try {
			setState(24);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(21);
				expr();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(22);
				apl(0);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(23);
				lam();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LamContext extends ParserRuleContext {
		public TerminalNode CBAR() { return getToken(hmParser.CBAR, 0); }
		public TerminalNode ID() { return getToken(hmParser.ID, 0); }
		public TerminalNode ARROW() { return getToken(hmParser.ARROW, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode LPAR() { return getToken(hmParser.LPAR, 0); }
		public LamContext lam() {
			return getRuleContext(LamContext.class,0);
		}
		public TerminalNode RPAR() { return getToken(hmParser.RPAR, 0); }
		public OperContext oper() {
			return getRuleContext(OperContext.class,0);
		}
		public LamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lam; }
	}

	public final LamContext lam() throws RecognitionException {
		LamContext _localctx = new LamContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_lam);
		try {
			setState(41);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(26);
				match(CBAR);
				setState(27);
				match(ID);
				setState(28);
				match(ARROW);
				setState(29);
				expr();
				setState(30);
				expr();
				setState(31);
				expr();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(33);
				match(LPAR);
				setState(34);
				lam();
				setState(35);
				match(RPAR);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(37);
				match(LPAR);
				setState(38);
				oper();
				setState(39);
				match(RPAR);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AplContext extends ParserRuleContext {
		public LamContext lam() {
			return getRuleContext(LamContext.class,0);
		}
		public AplContext apl() {
			return getRuleContext(AplContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AplContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_apl; }
	}

	public final AplContext apl() throws RecognitionException {
		return apl(0);
	}

	private AplContext apl(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		AplContext _localctx = new AplContext(_ctx, _parentState);
		AplContext _prevctx = _localctx;
		int _startState = 8;
		enterRecursionRule(_localctx, 8, RULE_apl, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(44);
			lam();
			}
			_ctx.stop = _input.LT(-1);
			setState(50);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new AplContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_apl);
					setState(46);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(47);
					expr();
					}
					} 
				}
				setState(52);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(hmParser.ID, 0); }
		public TerminalNode NUM() { return getToken(hmParser.NUM, 0); }
		public TerminalNode LPAR() { return getToken(hmParser.LPAR, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RPAR() { return getToken(hmParser.RPAR, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_expr);
		try {
			setState(59);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(53);
				match(ID);
				}
				break;
			case NUM:
				enterOuterAlt(_localctx, 2);
				{
				setState(54);
				match(NUM);
				}
				break;
			case LPAR:
				enterOuterAlt(_localctx, 3);
				{
				setState(55);
				match(LPAR);
				setState(56);
				expr();
				setState(57);
				match(RPAR);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperContext extends ParserRuleContext {
		public TerminalNode PLUS() { return getToken(hmParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(hmParser.MINUS, 0); }
		public TerminalNode MUL() { return getToken(hmParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(hmParser.DIV, 0); }
		public OperContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_oper; }
	}

	public final OperContext oper() throws RecognitionException {
		OperContext _localctx = new OperContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_oper);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 30L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 4:
			return apl_sempred((AplContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean apl_sempred(AplContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u000b@\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0004\u0001\u0012\b\u0001\u000b\u0001\f\u0001\u0013\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0003\u0002\u0019\b\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0003\u0003*\b\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0005\u00041\b\u0004\n\u0004\f\u00044\t\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0003\u0005<\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0000\u0001"+
		"\b\u0007\u0000\u0002\u0004\u0006\b\n\f\u0000\u0001\u0001\u0000\u0001\u0004"+
		"@\u0000\u000e\u0001\u0000\u0000\u0000\u0002\u0011\u0001\u0000\u0000\u0000"+
		"\u0004\u0018\u0001\u0000\u0000\u0000\u0006)\u0001\u0000\u0000\u0000\b"+
		"+\u0001\u0000\u0000\u0000\n;\u0001\u0000\u0000\u0000\f=\u0001\u0000\u0000"+
		"\u0000\u000e\u000f\u0003\u0002\u0001\u0000\u000f\u0001\u0001\u0000\u0000"+
		"\u0000\u0010\u0012\u0003\u0004\u0002\u0000\u0011\u0010\u0001\u0000\u0000"+
		"\u0000\u0012\u0013\u0001\u0000\u0000\u0000\u0013\u0011\u0001\u0000\u0000"+
		"\u0000\u0013\u0014\u0001\u0000\u0000\u0000\u0014\u0003\u0001\u0000\u0000"+
		"\u0000\u0015\u0019\u0003\n\u0005\u0000\u0016\u0019\u0003\b\u0004\u0000"+
		"\u0017\u0019\u0003\u0006\u0003\u0000\u0018\u0015\u0001\u0000\u0000\u0000"+
		"\u0018\u0016\u0001\u0000\u0000\u0000\u0018\u0017\u0001\u0000\u0000\u0000"+
		"\u0019\u0005\u0001\u0000\u0000\u0000\u001a\u001b\u0005\b\u0000\u0000\u001b"+
		"\u001c\u0005\t\u0000\u0000\u001c\u001d\u0005\u0007\u0000\u0000\u001d\u001e"+
		"\u0003\n\u0005\u0000\u001e\u001f\u0003\n\u0005\u0000\u001f \u0003\n\u0005"+
		"\u0000 *\u0001\u0000\u0000\u0000!\"\u0005\u0005\u0000\u0000\"#\u0003\u0006"+
		"\u0003\u0000#$\u0005\u0006\u0000\u0000$*\u0001\u0000\u0000\u0000%&\u0005"+
		"\u0005\u0000\u0000&\'\u0003\f\u0006\u0000\'(\u0005\u0006\u0000\u0000("+
		"*\u0001\u0000\u0000\u0000)\u001a\u0001\u0000\u0000\u0000)!\u0001\u0000"+
		"\u0000\u0000)%\u0001\u0000\u0000\u0000*\u0007\u0001\u0000\u0000\u0000"+
		"+,\u0006\u0004\uffff\uffff\u0000,-\u0003\u0006\u0003\u0000-2\u0001\u0000"+
		"\u0000\u0000./\n\u0002\u0000\u0000/1\u0003\n\u0005\u00000.\u0001\u0000"+
		"\u0000\u000014\u0001\u0000\u0000\u000020\u0001\u0000\u0000\u000023\u0001"+
		"\u0000\u0000\u00003\t\u0001\u0000\u0000\u000042\u0001\u0000\u0000\u0000"+
		"5<\u0005\t\u0000\u00006<\u0005\n\u0000\u000078\u0005\u0005\u0000\u0000"+
		"89\u0003\n\u0005\u00009:\u0005\u0006\u0000\u0000:<\u0001\u0000\u0000\u0000"+
		";5\u0001\u0000\u0000\u0000;6\u0001\u0000\u0000\u0000;7\u0001\u0000\u0000"+
		"\u0000<\u000b\u0001\u0000\u0000\u0000=>\u0007\u0000\u0000\u0000>\r\u0001"+
		"\u0000\u0000\u0000\u0005\u0013\u0018)2;";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}