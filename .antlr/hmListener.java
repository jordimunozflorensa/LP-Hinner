// Generated from /home/jordi/Escritorio/Jordi/q6/lp/lp_hinner/hm.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link hmParser}.
 */
public interface hmListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link hmParser#root}.
	 * @param ctx the parse tree
	 */
	void enterRoot(hmParser.RootContext ctx);
	/**
	 * Exit a parse tree produced by {@link hmParser#root}.
	 * @param ctx the parse tree
	 */
	void exitRoot(hmParser.RootContext ctx);
	/**
	 * Enter a parse tree produced by {@link hmParser#typing}.
	 * @param ctx the parse tree
	 */
	void enterTyping(hmParser.TypingContext ctx);
	/**
	 * Exit a parse tree produced by {@link hmParser#typing}.
	 * @param ctx the parse tree
	 */
	void exitTyping(hmParser.TypingContext ctx);
	/**
	 * Enter a parse tree produced by the {@code app}
	 * labeled alternative in {@link hmParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterApp(hmParser.AppContext ctx);
	/**
	 * Exit a parse tree produced by the {@code app}
	 * labeled alternative in {@link hmParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitApp(hmParser.AppContext ctx);
	/**
	 * Enter a parse tree produced by the {@code paren}
	 * labeled alternative in {@link hmParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterParen(hmParser.ParenContext ctx);
	/**
	 * Exit a parse tree produced by the {@code paren}
	 * labeled alternative in {@link hmParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitParen(hmParser.ParenContext ctx);
	/**
	 * Enter a parse tree produced by the {@code lambda}
	 * labeled alternative in {@link hmParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLambda(hmParser.LambdaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code lambda}
	 * labeled alternative in {@link hmParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLambda(hmParser.LambdaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code oper}
	 * labeled alternative in {@link hmParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterOper(hmParser.OperContext ctx);
	/**
	 * Exit a parse tree produced by the {@code oper}
	 * labeled alternative in {@link hmParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitOper(hmParser.OperContext ctx);
	/**
	 * Enter a parse tree produced by the {@code idexpr}
	 * labeled alternative in {@link hmParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterIdexpr(hmParser.IdexprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code idexpr}
	 * labeled alternative in {@link hmParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitIdexpr(hmParser.IdexprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code numexpr}
	 * labeled alternative in {@link hmParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNumexpr(hmParser.NumexprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code numexpr}
	 * labeled alternative in {@link hmParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNumexpr(hmParser.NumexprContext ctx);
}